# -*- coding: utf-8 -*-
import os

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

from service import CompartorService
from ui import Formatter
from utils import Files, Dialogs, Constant


# Form implementation generated from reading ui file 'd:\Development\smalltools\Python\CompareData\ui\Comparator.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 690)
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
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 605, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_1 = QtWidgets.QMenu(self.menuBar)
        self.menu_1.setObjectName("menu_1")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setStyleSheet("color: red;")
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_timestamp = QtWidgets.QAction(MainWindow)
        self.action_timestamp.setCheckable(True)
        self.action_timestamp.setChecked(True)
        self.action_timestamp.setObjectName("action_timestamp")
        self.action_file_formatter = QtWidgets.QAction(MainWindow)
        self.action_file_formatter.setObjectName("action_file_formatter")
        self.menu_2.addAction(self.action_file_formatter)
        self.menu_1.addAction(self.action_timestamp)
        self.menuBar.addAction(self.menu_1.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.open_plat_file_btn.clicked.connect(self.plat_file_clicked)
        self.open_his_file_btn.clicked.connect(self.his_file_clicked)
        self.open_template_file_btn.clicked.connect(self.template_file_clicked)
        self.clear_table_btn.clicked.connect(self.clear_table_clicked)
        self.execute_btn.clicked.connect(self.execute_clicked)
        self.action_file_formatter.triggered.connect(self.action_file_formatter_trigger)

    def plat_file_clicked(self):
        self.plat_file = Files.openfile()
        self.open_plat_thread = CompartorService.GetFileDataThread()
        self.open_plat_thread.set_values(self.plat_file)
        self.open_plat_thread.success.connect(self.open_plat_file_signal)
        self.open_plat_thread.error.connect(lambda e: Dialogs.error(e))
        self.open_plat_thread.start()
        self.statusBar.showMessage("已上传招采文件。")

    def open_plat_file_signal(self, data: pd.DataFrame):
        CompartorService.add_table_values(self.tableWidget, data, Constant.PLAT)
        self.plat_key_combo.addItems(data.columns)

    def his_file_clicked(self):
        self.his_file = Files.openfile()
        self.open_his_thread = CompartorService.GetFileDataThread()
        self.open_his_thread.set_values(self.his_file)
        self.open_his_thread.success.connect(self.open_his_file_signal)
        self.open_his_thread.error.connect(lambda e: Dialogs.error(e))
        self.open_his_thread.start()
        self.statusBar.showMessage("已上传 HIS 文件。")

    def open_his_file_signal(self, data: pd.DataFrame):
        CompartorService.add_table_values(self.tableWidget, data, Constant.HIS)
        self.his_key_combo.addItems(data.columns)

    def template_file_clicked(self):
        self.template_file = Files.openfile()
        self.open_template_thread = CompartorService.GetFileDataThread()
        self.open_template_thread.set_values(self.template_file)
        self.open_template_thread.success.connect(self.open_template_file_signal)
        self.open_template_thread.error.connect(lambda e: Dialogs.error(e))
        self.open_template_thread.start()

    def open_template_file_signal(self, data: pd.DataFrame):
        data.fillna('', inplace=True)
        self.tableWidget.setRowCount(0)
        self.reset_table_values(data)

        for i, v in data.iterrows():
            curr_row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(curr_row_count)

            self.tableWidget.setItem(curr_row_count, 0, CompartorService.not_edit_cell(v[Constant.TABLE_TYPE]))
            self.tableWidget.setItem(curr_row_count, 1, CompartorService.not_edit_cell(v[Constant.FIELD_NAME]))
            self.tableWidget.setItem(curr_row_count, 2, CompartorService.edit_cell(v[Constant.FILED_NEW_NAME]))
            self.tableWidget.setItem(curr_row_count, 3, CompartorService.edit_cell(v[Constant.AGG_CALC]))
            self.tableWidget.setItem(curr_row_count, 4, CompartorService.edit_cell(v[Constant.MATH_CALC]))
        self.statusBar.showMessage("已上传模板文件。")

    def clear_table_clicked(self):
        self.tableWidget.setRowCount(0)
        df = CompartorService.get_table_values(self.tableWidget)
        self.reset_table_values(df)

    def reset_table_values(self, df: pd.DataFrame):
        plat_keys: pd.DataFrame = df.loc[df[Constant.TABLE_TYPE] == Constant.PLAT]
        his_keys: pd.DataFrame = df.loc[df[Constant.TABLE_TYPE] == Constant.HIS]

        self.plat_key_combo.clear()
        self.plat_key_combo.addItems(plat_keys[Constant.FIELD_NAME].values)
        self.his_key_combo.clear()
        self.his_key_combo.addItems(his_keys[Constant.FIELD_NAME].values)
        self.statusBar.showMessage("已清除表格数据。")

    def execute_clicked(self):
        plat_key = self.plat_key_combo.currentText()
        his_key = self.his_key_combo.currentText()
        filename = self.output_filename_edit.text()
        df = CompartorService.get_table_values(self.tableWidget)

        self.execute_thread = CompartorService.ExecuteCompareThread()
        self.execute_thread.set_values(df, plat_key, his_key, self.plat_file, self.his_file, filename,
                                       self.action_timestamp.isChecked())
        self.execute_thread.error.connect(lambda e: Dialogs.error(e))
        self.execute_thread.success.connect(
            lambda e: Dialogs.menu(e, self.mission_success_to_open_file, self.mission_success_to_open_folder))
        self.execute_thread.start()

    def mission_success_to_open_file(self):
        filename = self.output_filename_edit.text()
        folder_path = Files.get_folder(self.plat_file)
        if self.action_timestamp.isChecked():
            output_path = os.path.join(folder_path, f"{filename}_差额对比表_{Files.format_time()}.xlsx")
        else:
            output_path = os.path.join(folder_path, f"{filename}_差额对比表.xlsx")
        self.statusBar.showMessage("已打开指定路径，本次操作已完成。")
        os.startfile(output_path)

    def mission_success_to_open_folder(self):
        folder_path = Files.get_folder(self.plat_file)
        self.statusBar.showMessage("已打开指定路径，本次操作已完成。")
        os.startfile(folder_path)

    def action_file_formatter_trigger(self):
        self.formatter = Formatter.Ui_MainWindow()
        self.formatter.window.show()
        self.statusBar.showMessage("已打开重组表格工具。")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "差额对比 V2.4.0 From 郑人滏"))
        self.label_1.setText(_translate("MainWindow", "上传"))
        self.open_plat_file_btn.setText(_translate("MainWindow", "上传招采文件"))
        self.open_his_file_btn.setText(_translate("MainWindow", "上传 HIS 文件"))
        self.open_template_file_btn.setText(_translate("MainWindow", "上传模板文件"))
        self.label_3.setText(_translate("MainWindow", "字段"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "表格类型"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "字段名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "字段新名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "聚合计算"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "逻辑计算"))
        self.clear_table_btn.setText(_translate("MainWindow", "清除表格"))
        self.label_2.setText(_translate("MainWindow", "连接"))
        self.plat_key_label.setText(_translate("MainWindow", "招采关键字"))
        self.his_key_label.setText(_translate("MainWindow", "HIS 关键字"))
        self.label_4.setText(_translate("MainWindow", "输出"))
        self.output_filename_label.setText(_translate("MainWindow", "文件名"))
        self.execute_btn.setText(_translate("MainWindow", "执行任务"))
        self.menu_2.setTitle(_translate("MainWindow", "工具"))
        self.menu_1.setTitle(_translate("MainWindow", "设置"))
        self.action_timestamp.setText(_translate("MainWindow", "文件名携带时间戳"))
        self.action_file_formatter.setText(_translate("MainWindow", "打开重组表格工具"))
