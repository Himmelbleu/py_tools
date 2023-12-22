import os
import re

import pandas as pd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow

import common.utils as utils


class CompareThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str, name='CompareThread')
    source_code = ''
    output_path = ''
    input_path = ''

    def set_values(self, source_code, output_path, input_path):
        self.source_code = source_code
        self.output_path = output_path
        self.input_path = input_path

    def run(self):
        output_path = self.output_path
        data = pd.read_excel(self.input_path, sheet_name=None)
        try:
            exec(self.source_code)
        except Exception as e:
            error_message = str(e)
            self.signal.emit(error_message)


def execute(self: QMainWindow | QMainWindow, filepath: str, text_edit: QtWidgets.QTextEdit):
    filename = re.findall(r'[^\\/:*?"<>|\r\n]+$', filepath)[0].split('.')[0]
    source_code = text_edit.toPlainText()
    folder_path = "/".join(filepath.split("/")[:-1]) + "/"
    output_path = os.path.join(folder_path, f"{filename}_差额对比表_{utils.format_time()}.xlsx")

    self.thread = CompareThread()
    self.thread.set_values(source_code=source_code, input_path=filepath, output_path=output_path)
    self.thread.start()


def openfile(self: QMainWindow | QMainWindow):
    filepath = QFileDialog.getOpenFileName(None, "选择 Excel 文件", "", "Excel 文件 (*.xlsx *.xls)")
    if filepath:
        self.filepath = filepath[0]
