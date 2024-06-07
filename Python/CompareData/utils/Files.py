import re
from datetime import datetime

import win32com.client as win32
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


def to_xls(xml_file, xls_file):
    # 创建 Excel 应用程序对象
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    excel.Visible = False

    try:
        # 打开 XML 文件
        workbook = excel.Workbooks.Open(xml_file)

        # 保存为 XLS 文件格式
        workbook.SaveAs(xls_file, FileFormat=56)

        # 关闭工作簿，不保存更改
        workbook.Close(False)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # 退出 Excel 应用程序
        excel.Application.Quit()

        # 确保释放所有 COM 对象
        del workbook
        del excel
