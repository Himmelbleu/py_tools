# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Projects\PythonProjects\deciphering\myui.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import copy_signal_file


class OpenFileDialogThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str, name='OpenFileDialogThread')
    file_type = "解密单个文件路径"

    def run(self):
        if self.file_type == "解密单个文件路径":
            options = QtWidgets.QFileDialog.Options()
            file_path, _ = QtWidgets.QFileDialog().getOpenFileName(None, "选择文件", "",
                                                                   "All Files (*);;Python Files (*.py)",
                                                                   options=options)
            if file_path:
                self.signal.emit(file_path)
        else:
            options = QFileDialog.Options()
            folder_path = QFileDialog.getExistingDirectory(options=options)

            if folder_path:
                self.signal.emit(folder_path)


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(777, 500)
        self.main_widget = QtWidgets.QWidget(main_window)
        self.main_widget.setObjectName("main_widget")
        self.decrypt_signal_file = QtWidgets.QRadioButton(self.main_widget)
        self.decrypt_signal_file.setGeometry(QtCore.QRect(20, 20, 115, 19))
        self.decrypt_signal_file.setChecked(True)
        self.decrypt_signal_file.setObjectName("decrypt_signal_file")
        self.decrypt_multi_files = QtWidgets.QRadioButton(self.main_widget)
        self.decrypt_multi_files.setGeometry(QtCore.QRect(180, 20, 211, 19))
        self.decrypt_multi_files.setObjectName("decrypt_multi_files")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_widget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 50, 741, 391))
        self.stackedWidget.setObjectName("stackedWidget")
        self.signal_file_page = QtWidgets.QWidget()
        self.signal_file_page.setObjectName("signal_file_page")
        self.signal_file_select_btn = QtWidgets.QPushButton(self.signal_file_page)
        self.signal_file_select_btn.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.signal_file_select_btn.setObjectName("signal_file_select_btn")
        self.signal_file_decrypt_dest_path_btn = QtWidgets.QPushButton(self.signal_file_page)
        self.signal_file_decrypt_dest_path_btn.setGeometry(QtCore.QRect(10, 60, 93, 28))
        self.signal_file_decrypt_dest_path_btn.setObjectName("signal_file_decrypt_dest_path_btn")
        self.signal_file_text_area = QtWidgets.QTextBrowser(self.signal_file_page)
        self.signal_file_text_area.setGeometry(QtCore.QRect(10, 110, 721, 192))
        self.signal_file_text_area.setObjectName("signal_file_text_area")
        self.signal_file_path_label = QtWidgets.QLabel(self.signal_file_page)
        self.signal_file_path_label.setGeometry(QtCore.QRect(120, 10, 611, 28))
        self.signal_file_path_label.setText("")
        self.signal_file_path_label.setObjectName("signal_file_path_label")
        self.signal_file_path_dest_label = QtWidgets.QLabel(self.signal_file_page)
        self.signal_file_path_dest_label.setGeometry(QtCore.QRect(120, 60, 611, 28))
        self.signal_file_path_dest_label.setText("")
        self.signal_file_path_dest_label.setObjectName("signal_file_path_dest_label")
        self.start_decrypt_signal_file = QtWidgets.QPushButton(self.signal_file_page)
        self.start_decrypt_signal_file.setGeometry(QtCore.QRect(640, 340, 93, 28))
        self.start_decrypt_signal_file.setObjectName("start_decrypt_signal_file")
        self.stackedWidget.addWidget(self.signal_file_page)
        self.multi_files_page = QtWidgets.QWidget()
        self.multi_files_page.setObjectName("multi_files_page")
        self.stackedWidget.addWidget(self.multi_files_page)
        main_window.setCentralWidget(self.main_widget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 777, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(main_window)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.decrypt_signal_file.toggled.connect(self.on_radio_button_toggled)
        self.decrypt_multi_files.toggled.connect(self.on_radio_button_toggled)
        self.signal_file_select_btn.clicked.connect(self.on_signal_file_select_btn)
        self.signal_file_decrypt_dest_path_btn.clicked.connect(self.on_decrypt_dest_path_btn)
        self.start_decrypt_signal_file.clicked.connect(self.on_start_decrypt_signal_file)

    def on_radio_button_toggled(self):
        if self.decrypt_signal_file.isChecked():
            self.stackedWidget.setCurrentIndex(0)  # Index of the first layout
        elif self.decrypt_multi_files.isChecked():
            self.stackedWidget.setCurrentIndex(1)  # Index of the second layout

    def on_signal_file_select_btn(self):
        self.open_file_dialog_thread = OpenFileDialogThread()
        self.open_file_dialog_thread.signal.connect(self.after_selected_signal_file_path)
        self.open_file_dialog_thread.file_type = "解密单个文件路径"
        self.open_file_dialog_thread.start()

    def after_selected_signal_file_path(self, file_path):
        self.signal_file_path_label.setText(file_path)

    def on_decrypt_dest_path_btn(self):
        self.open_file_dialog_thread = OpenFileDialogThread()
        self.open_file_dialog_thread.signal.connect(self.after_selected_decrypt_dest_path)
        self.open_file_dialog_thread.file_type = "存放解密文件的路径"
        self.open_file_dialog_thread.start()

    def after_selected_decrypt_dest_path(self, file_path):
        self.signal_file_path_dest_label.setText(file_path)

    def on_start_decrypt_signal_file(self):
        copy_signal_file.decrypt_signal_file(self.signal_file_path_label.text(),
                                             self.signal_file_path_dest_label.text(),
                                             lambda x: self.signal_file_text_area.append(x + "\n"))

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "文件解密器"))
        self.decrypt_signal_file.setText(_translate("main_window", "解密单个文件"))
        self.decrypt_multi_files.setText(_translate("main_window", "解密文件夹下所有文件"))
        self.signal_file_select_btn.setText(_translate("main_window", "选择文件"))
        self.signal_file_decrypt_dest_path_btn.setText(_translate("main_window", "解密位置"))
        self.start_decrypt_signal_file.setText(_translate("main_window", "开始解密"))
        self.menu.setTitle(_translate("main_window", "选项"))