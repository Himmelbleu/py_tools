from PyQt5.QtWidgets import QMessageBox


def error(msg):
    QMessageBox.critical(None, "Error", f"Type: {type(msg)}\n\nInfo: \n{str(msg)}", QMessageBox.Ok)


def info(msg):
    QMessageBox.information(None, 'Success', f'Info: \n\n{msg}\n\n', QMessageBox.Ok)


def information(msg):
    QMessageBox.information(None, 'Info', f'{msg}\n\n', QMessageBox.Ok)


def menu(msg, open_file, open_folder):
    msg_box = QMessageBox(QMessageBox.Information, 'Success', f'Info: \n{msg}\n\n')
    btn1 = msg_box.addButton('打开该文件', QMessageBox.YesRole)
    btn2 = msg_box.addButton('打开文件夹', QMessageBox.YesRole)
    btn3 = msg_box.addButton('关闭对话框', QMessageBox.YesRole)

    msg_box.exec_()

    if msg_box.clickedButton() == btn1:
        open_file()
    elif msg_box.clickedButton() == btn2:
        open_folder()
    elif msg_box.clickedButton() == btn3:
        msg_box.close()
