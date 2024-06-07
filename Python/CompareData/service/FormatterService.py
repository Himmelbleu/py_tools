import os

import pandas as pd
from PyQt5 import QtCore

from utils import Files


class FormatThread(QtCore.QThread):
    error = QtCore.pyqtSignal(Exception, name='error')
    success = QtCore.pyqtSignal(str, name='success')

    def set_values(self, filepath):
        self.filepath = filepath

    def run(self):
        path = os.path.join(Files.get_folder(self.filepath),
                            f"{Files.get_filename(self.filepath)}_新建_{Files.format_time()}.xls").replace('/', '\\')
        Files.to_xls(self.filepath, path)
        data = pd.read_excel(path, converters={'国家医保编码': str, '药品监管码': str})

        try:
            supplier = ''
            project_type = ''
            health_code = ''
            project_name = ''
            is_base = ''
            monitoring_code = ''
            specifications = ''
            lot_number = ''
            manufacturer = ''
            project_number = ''
            approval_number = ''
            author = ''
            volume_based_procurement = ''

            new_data = []

            for index, row in data.iterrows():
                if str(row['入库数量']) == 'nan':
                    project_type = ''
                    health_code = ''
                    project_name = ''
                    is_base = ''
                    monitoring_code = ''
                    specifications = ''
                    lot_number = ''
                    manufacturer = ''
                    project_number = ''
                    approval_number = ''
                    author = ''
                    volume_based_procurement = ''
                    continue

                if str(row['供货单位']) != 'nan':
                    supplier = row['供货单位']
                else:
                    row['供货单位'] = supplier

                if str(row['项目类型']) != 'nan':
                    project_type = row['项目类型']
                else:
                    row['项目类型'] = project_type

                if str(row['国家医保编码']) != 'nan':
                    health_code = row['国家医保编码']
                else:
                    row['国家医保编码'] = health_code

                if str(row['项目名称']) != 'nan':
                    project_name = row['项目名称']
                else:
                    row['项目名称'] = project_name

                if str(row['是否基药']) != 'nan':
                    is_base = row['是否基药']
                else:
                    row['是否基药'] = is_base

                if str(row['药品监管码']) != 'nan':
                    monitoring_code = row['药品监管码']
                else:
                    row['药品监管码'] = monitoring_code

                if str(row['规格']) != 'nan':
                    specifications = row['规格']
                else:
                    row['规格'] = specifications

                if str(row['生产批号']) != 'nan':
                    lot_number = row['生产批号']
                else:
                    row['生产批号'] = lot_number

                if str(row['生产厂家']) != 'nan':
                    manufacturer = row['生产厂家']
                else:
                    row['生产厂家'] = manufacturer

                if str(row['项目编码']) != 'nan':
                    project_number = row['项目编码']
                else:
                    row['项目编码'] = project_number

                if str(row['批准文号']) != 'nan':
                    approval_number = row['批准文号']
                else:
                    row['批准文号'] = approval_number

                if str(row['操作人']) != 'nan':
                    author = row['操作人']
                else:
                    row['操作人'] = author

                if str(row['带量采购']) != 'nan':
                    volume_based_procurement = row['带量采购']
                else:
                    row['带量采购'] = volume_based_procurement

                new_data.append(row)

            output_path = os.path.join(Files.get_folder(self.filepath),
                                       f"{Files.get_filename(self.filepath)}_格式化_{Files.format_time()}.xlsx")
            pd.DataFrame(new_data).to_excel(rf"{output_path}", index=False)

            self.success.emit(output_path)
        except Exception as error_msg:
            self.error.emit(error_msg)
