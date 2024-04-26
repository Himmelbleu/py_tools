# -*- coding: utf-8 -*-
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

from consts import Consts
from service import Services


# Form implementation generated from reading ui file 'd:\Development\MyTools\Python\CompareData\ui\UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 689)
        self.verticalLayout_1 = QtWidgets.QWidget(MainWindow)
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.v_2 = QtWidgets.QVBoxLayout(self.verticalLayout_1)
        self.v_2.setContentsMargins(9, -1, -1, -1)
        self.v_2.setSpacing(30)
        self.v_2.setObjectName("v_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_1 = QtWidgets.QLabel(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_2.addWidget(self.label_1)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.open_plat_file_btn = QtWidgets.QPushButton(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.open_plat_file_btn.setFont(font)
        self.open_plat_file_btn.setObjectName("open_plat_file_btn")
        self.horizontalLayout_1.addWidget(self.open_plat_file_btn)
        self.open_his_file_btn = QtWidgets.QPushButton(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.open_his_file_btn.setFont(font)
        self.open_his_file_btn.setIconSize(QtCore.QSize(16, 16))
        self.open_his_file_btn.setObjectName("open_his_file_btn")
        self.horizontalLayout_1.addWidget(self.open_his_file_btn)
        self.open_template_file_btn = QtWidgets.QPushButton(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.open_template_file_btn.setFont(font)
        self.open_template_file_btn.setObjectName("open_template_file_btn")
        self.horizontalLayout_1.addWidget(self.open_template_file_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_1)
        self.v_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_field_btn = QtWidgets.QPushButton(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_field_btn.setFont(font)
        self.add_field_btn.setObjectName("add_field_btn")
        self.horizontalLayout.addWidget(self.add_field_btn)
        self.del_select_btn = QtWidgets.QPushButton(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.del_select_btn.setFont(font)
        self.del_select_btn.setObjectName("del_select_btn")
        self.horizontalLayout.addWidget(self.del_select_btn)
        self.clear_table_btn = QtWidgets.QPushButton(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clear_table_btn.setFont(font)
        self.clear_table_btn.setAutoFillBackground(False)
        self.clear_table_btn.setStyleSheet("")
        self.clear_table_btn.setObjectName("clear_table_btn")
        self.horizontalLayout.addWidget(self.clear_table_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.v_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayout_1)
        self.label_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plat_key_label = QtWidgets.QLabel(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plat_key_label.setFont(font)
        self.plat_key_label.setObjectName("plat_key_label")
        self.horizontalLayout_2.addWidget(self.plat_key_label)
        self.plat_key_combo = QtWidgets.QComboBox(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plat_key_combo.setFont(font)
        self.plat_key_combo.setObjectName("plat_key_combo")
        self.horizontalLayout_2.addWidget(self.plat_key_combo)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.his_key_label = QtWidgets.QLabel(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.his_key_label.setFont(font)
        self.his_key_label.setObjectName("his_key_label")
        self.horizontalLayout_3.addWidget(self.his_key_label)
        self.his_key_combo = QtWidgets.QComboBox(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.his_key_combo.setFont(font)
        self.his_key_combo.setObjectName("his_key_combo")
        self.horizontalLayout_3.addWidget(self.his_key_combo)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.v_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.output_filename_label = QtWidgets.QLabel(self.verticalLayout_1)
        self.output_filename_label.setObjectName("output_filename_label")
        self.horizontalLayout_4.addWidget(self.output_filename_label)
        self.output_filename_edit = QtWidgets.QLineEdit(self.verticalLayout_1)
        self.output_filename_edit.setObjectName("output_filename_edit")
        self.horizontalLayout_4.addWidget(self.output_filename_edit)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.execute_btn = QtWidgets.QPushButton(self.verticalLayout_1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.execute_btn.setFont(font)
        self.execute_btn.setObjectName("execute_btn")
        self.verticalLayout_5.addWidget(self.execute_btn)
        self.v_2.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.verticalLayout_1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.open_plat_file_btn.clicked.connect(self.open_plat_file)
        self.open_his_file_btn.clicked.connect(self.open_his_file)
        self.open_template_file_btn.clicked.connect(self.open_template_file)
        self.add_field_btn.clicked.connect(lambda: Services.add_table_value(self.tableWidget))
        self.clear_table_btn.clicked.connect(self.clear_all_table_rows)
        self.del_select_btn.clicked.connect(self.clear_select_table_rows)
        self.execute_btn.clicked.connect(self.execute_mission)

    def open_plat_file(self):
        self.plat_file = Services.openfile()
        self.open_plat_thread = Services.GetFileDataThread()
        self.open_plat_thread.set_values(self.plat_file)
        self.open_plat_thread.success_signal.connect(self.open_plat_file_signal)
        self.open_plat_thread.error_signal.connect(lambda e: Services.error_signal(e))
        self.open_plat_thread.start()

    def open_plat_file_signal(self, data: pd.DataFrame):
        Services.add_table_values(self.tableWidget, data, Consts.PLAT)
        self.plat_key_combo.addItems(data.columns)

    def open_his_file(self):
        self.his_file = Services.openfile()
        self.open_his_thread = Services.GetFileDataThread()
        self.open_his_thread.set_values(self.his_file)
        self.open_his_thread.success_signal.connect(self.open_his_file_signal)
        self.open_his_thread.error_signal.connect(lambda e: Services.error_signal(e))
        self.open_his_thread.start()

    def open_his_file_signal(self, data: pd.DataFrame):
        Services.add_table_values(self.tableWidget, data, Consts.HIS)
        self.his_key_combo.addItems(data.columns)

    def open_template_file(self):
        self.template_file = Services.openfile()
        self.open_template_thread = Services.GetFileDataThread()
        self.open_template_thread.set_values(self.template_file)
        self.open_template_thread.success_signal.connect(self.open_template_file_signal)
        self.open_template_thread.error_signal.connect(lambda e: Services.error_signal(e))
        self.open_template_thread.start()

    def open_template_file_signal(self, data: pd.DataFrame):
        data.fillna('', inplace=True)
        self.tableWidget.setRowCount(0)
        self.reset_table_values(data)

        for i, v in data.iterrows():
            curr_row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(curr_row_count)

            self.tableWidget.setItem(curr_row_count, 0, Services.not_edit_cell(v[Consts.FIELD_TABLE_NAME]))
            self.tableWidget.setItem(curr_row_count, 1, Services.not_edit_cell(v[Consts.FIELD_NAME]))
            self.tableWidget.setItem(curr_row_count, 2, Services.edit_cell(v[Consts.FILED_NEW_NAME]))
            self.tableWidget.setItem(curr_row_count, 3, Services.edit_cell(v[Consts.FILED_AGG]))
            self.tableWidget.setItem(curr_row_count, 4, Services.edit_cell(v[Consts.FILED_MATH]))

    def clear_all_table_rows(self):
        self.tableWidget.setRowCount(0)
        df = Services.get_table_values(self.tableWidget)
        self.reset_table_values(df)

    def clear_select_table_rows(self):
        idxs = set(index.row() for index in self.tableWidget.selectedIndexes())
        for i in sorted(idxs, reverse=True):
            self.tableWidget.removeRow(i)

        df = Services.get_table_values(self.tableWidget)
        self.reset_table_values(df)

    def reset_table_values(self, df: pd.DataFrame):
        plat_keys: pd.DataFrame = df.loc[df[Consts.FIELD_TABLE_NAME] == Consts.PLAT]
        his_keys: pd.DataFrame = df.loc[df[Consts.FIELD_TABLE_NAME] == Consts.HIS]

        self.plat_key_combo.clear()
        self.his_key_combo.clear()
        self.plat_key_combo.addItems(plat_keys[Consts.FIELD_NAME].values)
        self.his_key_combo.addItems(his_keys[Consts.FIELD_NAME].values)

    def execute_mission(self):
        plat_key = self.plat_key_combo.currentText()
        his_key = self.his_key_combo.currentText()
        output_filename = self.output_filename_edit.text()
        df = Services.get_table_values(self.tableWidget)

        self.execute_thread = Services.ExecuteCompareThread()
        self.execute_thread.set_values(df, plat_key, his_key, self.plat_file, self.his_file, output_filename)
        self.execute_thread.error_signal.connect(lambda e: Services.error_signal(e))
        self.execute_thread.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "差额对比-v2.2.0-Create By 郑人滏"))
        self.label_1.setText(_translate("MainWindow", "上传"))
        self.open_plat_file_btn.setText(_translate("MainWindow", "上传招采文件"))
        self.open_his_file_btn.setText(_translate("MainWindow", "上传 HIS 文件"))
        self.open_template_file_btn.setText(_translate("MainWindow", "上传模板文件"))
        self.label_3.setText(_translate("MainWindow", "字段"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "所属表名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "字段名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "字段新名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "聚合计算"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "逻辑计算"))
        self.add_field_btn.setText(_translate("MainWindow", "添加一行"))
        self.del_select_btn.setText(_translate("MainWindow", "删除所选行"))
        self.clear_table_btn.setText(_translate("MainWindow", "清除表格"))
        self.label_2.setText(_translate("MainWindow", "连接"))
        self.plat_key_label.setText(_translate("MainWindow", "招采关键字"))
        self.his_key_label.setText(_translate("MainWindow", "HIS 关键字"))
        self.label_4.setText(_translate("MainWindow", "输出"))
        self.output_filename_label.setText(_translate("MainWindow", "输出文件名"))
        self.execute_btn.setText(_translate("MainWindow", "执行任务"))