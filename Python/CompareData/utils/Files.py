import os
import re
from datetime import datetime

import win32com.client as win32
from PyQt5.QtWidgets import QFileDialog

from utils import Dialogs


def openfile():
    filepath = QFileDialog.getOpenFileName(None, "", "", "(*.xlsx *.xls)")
    if filepath:
        return filepath[0]


def get_filename(filepath: str):
    filename = re.findall(r'[^\\/:*?"<>|\r\n]+$', filepath)[0].split('.')[0]
    return filename


def get_folder(filepath: str):
    folder_path = os.path.dirname(filepath)
    return folder_path


def format_time(_formatter="%m-%d-%H-%M"):
    return datetime.now().strftime(_formatter)


def to_xls(input_file, output_file):
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = False

    try:
        workbook = excel.Workbooks.Open(input_file)
        workbook.SaveAs(output_file, FileFormat=51)
        workbook.Close(False)
    except Exception as e:
        Dialogs.error(e)
    finally:
        excel.Application.Quit()
        del workbook
        del excel
