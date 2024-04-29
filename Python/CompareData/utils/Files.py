import re
from datetime import datetime

from PyQt5.QtWidgets import QFileDialog


def openfile():
    filepath = QFileDialog.getOpenFileName(None, "", "", "(*.xlsx *.xls)")
    if filepath:
        return filepath[0]


def get_filename(filepath: str):
    filename = re.findall(r'[^\\/:*?"<>|\r\n]+$', filepath)[0].split('.')[0]
    return filename


def get_folder(filepath: str):
    folder_path = "/".join(filepath.split("/")[:-1]) + "/"
    return folder_path


def format_time(_formatter="%m-%d-%H-%M"):
    return datetime.now().strftime(_formatter)
