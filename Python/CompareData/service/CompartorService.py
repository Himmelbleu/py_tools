import os

import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem

from utils import Maths, Files, Constant


class GetFileDataThread(QtCore.QThread):
    error = QtCore.pyqtSignal(Exception, name='error')
    success = QtCore.pyqtSignal(pd.DataFrame, name='success')

    def set_values(self, input_path):
        self.input_path = input_path

    def run(self):
        try:
            df = Maths.validate(pd.read_excel(self.input_path))
            self.success.emit(df)
        except Exception as error_msg:
            self.error.emit(error_msg)


class ExecuteCompareThread(QtCore.QThread):
    error = QtCore.pyqtSignal(Exception, name='error')
    success = QtCore.pyqtSignal(str, name='success')

    def set_values(self, df_data, plat_key, his_key, plat_file, his_file, filename, is_timestamp):
        self.df_data = df_data
        self.plat_key = plat_key
        self.his_key = his_key
        self.plat_file = plat_file
        self.his_file = his_file
        self.filename = filename
        self.is_timestamp = is_timestamp

    def exec_context(self, df: pd.DataFrame, col: str, formula: str):
        exec(f"df['{col}'] = {formula}")
        return df

    def pretreatment(self, df_cols: pd.DataFrame, df: pd.DataFrame):
        df_cols[Constant.FILED_NEW_NAME].replace('', np.nan, inplace=True)
        df_cols[Constant.FILED_NEW_NAME].fillna(df_cols[Constant.FIELD_NAME], inplace=True)

        for _, val in df_cols.iterrows():
            df.rename(columns={val[Constant.FIELD_NAME]: val[Constant.FILED_NEW_NAME]}, inplace=True)
            if val[Constant.MATH_CALC]:
                df = self.exec_context(df, val[Constant.FILED_NEW_NAME], val[Constant.MATH_CALC])

        return df

    def run(self):
        try:
            if not bool(self.filename.strip()):
                raise ValueError('输出的文件名称不能空！')

            plat_data = Maths.validate(pd.read_excel(self.plat_file))
            if plat_data.empty:
                raise ValueError('招采的数据不能空！')

            his_data = Maths.validate(pd.read_excel(self.his_file))
            if his_data.empty:
                raise ValueError('HIS 的数据不能空！')

            plat_cols = Maths.validate(
                self.df_data.loc[self.df_data[Constant.TABLE_TYPE] == Constant.PLAT])
            his_cols = Maths.validate(
                self.df_data.loc[self.df_data[Constant.TABLE_TYPE] == Constant.HIS])

            pre_plat_data = self.pretreatment(plat_cols, plat_data)
            pre_his_data = self.pretreatment(his_cols, his_data)

            agg_plat_data = pre_plat_data.groupby(self.plat_key).agg(get_dict(plat_cols))
            agg_his_data = pre_his_data.groupby(self.his_key).agg(get_dict(his_cols))

            agg_plat_data.reset_index(drop=True, inplace=True)
            agg_his_data.reset_index(drop=True, inplace=True)
            merged_data = pd.merge(agg_plat_data, agg_his_data, how='outer', indicator='匹配情况',
                                   left_on=self.plat_key, right_on=self.his_key)

            combine_cols = Maths.validate(self.df_data.loc[self.df_data[Constant.TABLE_TYPE] == ''])
            pre_combine_data = self.pretreatment(combine_cols, merged_data)
            pre_combine_data['匹配情况'].replace(
                {'left_only': '只在招采', 'right_only': '只在HIS', 'both': '两者共有'}, inplace=True)
            if self.is_timestamp:
                output_path = os.path.join(Files.get_folder(self.plat_file),
                                           f"{self.filename}_差额对比表_{Files.format_time()}.xlsx")
            else:
                output_path = os.path.join(Files.get_folder(self.plat_file),
                                           f"{self.filename}_差额对比表.xlsx")
            pre_combine_data.to_excel(output_path, index=False)

            self.success.emit(output_path)
        except Exception as error_msg:
            self.error.emit(error_msg)


def not_edit_cell(val: str):
    item = QTableWidgetItem(val)
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
        table.setItem(curr_row_count, 2, not_edit_cell(i))
        table.setItem(curr_row_count, 3, not_edit_cell(i))
        table.setItem(curr_row_count, 4, not_edit_cell(i))


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
                        columns=[Constant.TABLE_TYPE, Constant.FIELD_NAME, Constant.FILED_NEW_NAME, Constant.AGG_CALC,
                                 Constant.MATH_CALC])


def get_dict(df: pd.DataFrame):
    dictionary = {}
    for k, v in zip(df[Constant.FILED_NEW_NAME], df[Constant.AGG_CALC]):
        if v != '':
            if v in Constant.NOT_TO_EVAL:
                dictionary[k] = v
            else:
                dictionary[k] = eval(v)

    return dictionary
