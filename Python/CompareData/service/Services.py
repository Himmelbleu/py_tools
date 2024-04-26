import os

import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem

from consts import Consts
from utils import Utils


class GetFileDataThread(QtCore.QThread):
    error_signal = QtCore.pyqtSignal(Exception, name='error_signal')
    success_signal = QtCore.pyqtSignal(pd.DataFrame, name='success_signal')

    def set_values(self, input_path):
        self.input_path = input_path

    def run(self):
        try:
            df = Utils.validate(pd.read_excel(self.input_path))
            self.success_signal.emit(df)
        except Exception as error_message:
            self.error_signal.emit(error_message)


class ExecuteCompareThread(QtCore.QThread):
    error_signal = QtCore.pyqtSignal(Exception, name='error_signal')
    success_signal = QtCore.pyqtSignal(str, name='success_signal')

    def set_values(self, df_data, plat_key, his_key, plat_file, his_file, output_filename):
        self.df_data = df_data
        self.plat_key = plat_key
        self.his_key = his_key
        self.plat_file = plat_file
        self.his_file = his_file
        self.output_filename = output_filename

    def parse_and_execute(self, df: pd.DataFrame, col: str, formula: str):
        exec(f"df['{col}'] = {formula}")
        return df

    def math_calc(self, df_keys: pd.DataFrame, df: pd.DataFrame):
        df_keys[Consts.FILED_NEW_NAME].replace('', np.nan, inplace=True)
        df_keys[Consts.FILED_NEW_NAME].fillna(df_keys[Consts.FIELD_NAME], inplace=True)
        for i, v in df_keys.iterrows():
            df.rename(columns={v[Consts.FIELD_NAME]: v[Consts.FILED_NEW_NAME]}, inplace=True)
            if v[Consts.FILED_MATH]:
                df = self.parse_and_execute(df, v[Consts.FILED_NEW_NAME], v[Consts.FILED_MATH])
        return df

    def run(self):
        try:
            plat_data = Utils.validate(pd.read_excel(self.plat_file))
            if plat_data.empty:
                raise ValueError('招采的数据不能空！')

            his_data = Utils.validate(pd.read_excel(self.his_file))
            if his_data.empty:
                raise ValueError('HIS 的数据不能空！')

            plat_keys: pd.DataFrame = Utils.validate(
                self.df_data.loc[self.df_data[Consts.FIELD_TABLE_NAME] == Consts.PLAT])
            his_keys: pd.DataFrame = Utils.validate(
                self.df_data.loc[self.df_data[Consts.FIELD_TABLE_NAME] == Consts.HIS])
            combine_keys: pd.DataFrame = Utils.validate(self.df_data.loc[self.df_data[Consts.FIELD_TABLE_NAME] == ''])

            # 逻辑计算
            plat_data = self.math_calc(plat_keys, plat_data)
            his_data = self.math_calc(his_keys, his_data)

            agg_plat_cols = get_new_dict(plat_keys)
            if not agg_plat_cols:
                raise ValueError('招采的聚合计算列不能空！')

            agg_his_cols = get_new_dict(his_keys)
            if not agg_his_cols:
                raise ValueError('HIS 的聚合计算列不能空！')

            # 聚合计算
            agg_plat_data = plat_data.groupby(self.plat_key).agg(agg_plat_cols)
            agg_his_data = his_data.groupby(self.his_key).agg(agg_his_cols)

            # 连接
            agg_plat_data.reset_index(drop=True, inplace=True)
            agg_his_data.reset_index(drop=True, inplace=True)
            merged_data = pd.merge(agg_plat_data, agg_his_data,
                                   how='outer', indicator='匹配情况',
                                   left_on=self.plat_key, right_on=self.his_key)

            # 逻辑计算
            merged_data = self.math_calc(combine_keys, merged_data)
            merged_data['匹配情况'].replace(
                {'left_only': '只存在于招采', 'right_only': '只存在于HIS', 'both': '招采与HIS共有'}, inplace=True)

            # 输出文件
            folder_path = Utils.get_folder(self.plat_file)
            output_path = os.path.join(folder_path, f"{self.output_filename}_差额对比表_{Utils.format_time()}.xlsx")
            merged_data.to_excel(output_path, index=False)

            self.success_signal.emit('')
        except Exception as error_msg:
            self.error_signal.emit(error_msg)


def openfile():
    filepath = QFileDialog.getOpenFileName(None, "选择 Excel", "", "Excel (*.xlsx *.xls)")
    if filepath:
        return filepath[0]


def not_edit_cell(val: str):
    item = QTableWidgetItem(val)
    item.setBackground(QColor(220, 220, 220, 50))
    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
    return item


def edit_cell(val: str):
    return QTableWidgetItem(val)


def add_table_values(table: QtWidgets.QTableWidget, df: pd.DataFrame, col_val: str):
    for i in df.columns:
        curr_row_count = table.rowCount()
        table.insertRow(curr_row_count)

        table.setItem(curr_row_count, 0, not_edit_cell(col_val))
        table.setItem(curr_row_count, 1, not_edit_cell(i))


def add_table_value(table: QtWidgets.QTableWidget):
    curr_row_count = table.rowCount()
    table.insertRow(curr_row_count)

    table.setItem(curr_row_count, 0, not_edit_cell(''))
    table.setItem(curr_row_count, 1, edit_cell(''))
    table.setItem(curr_row_count, 2, not_edit_cell(''))
    table.setItem(curr_row_count, 3, not_edit_cell(''))


def get_table_values(table: QtWidgets.QTableWidget):
    table_values = []
    rows = table.rowCount()
    cols = table.columnCount()

    for row in range(rows):
        values = []
        for column in range(cols):
            item = table.item(row, column)
            if item is not None:
                values.append(item.text())
            else:
                values.append("")
        table_values.append(values)

    return pd.DataFrame(table_values,
                        columns=[Consts.FIELD_TABLE_NAME, Consts.FIELD_NAME, Consts.FILED_NEW_NAME, Consts.FILED_AGG,
                                 Consts.FILED_MATH])


def get_new_dict(df_keys: pd.DataFrame):
    return {key: value for key, value in
            zip(df_keys[Consts.FILED_NEW_NAME], df_keys[Consts.FILED_AGG]) if
            value != ''}


def error_signal(error_msg):
    QMessageBox.critical(None,
                         "Error",
                         f"Type: {type(error_msg)}"
                         f"\n\nInfo: \n{str(error_msg)}",
                         QMessageBox.Ok)
