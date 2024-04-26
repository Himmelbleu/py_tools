import builtins
import re
from datetime import datetime

import pandas as pd


def reserve(number, decimal_places=2):
    result = builtins.round(number, decimal_places)
    return int(result) if result.is_integer() else result


def percentage(_numerator, _denominator):
    if _denominator != 0:
        return (_numerator / _denominator) * 100
    else:
        return 0


def digitize(_text):
    match = re.search(r'[-+]?\d+', str(_text))
    if match:
        return float(match.group(0))
    return 0


def validate(df: pd.DataFrame):
    df.columns = df.columns.str.replace('[\(\[（]', '_', regex=True).str.replace('[\)\]）]', '', regex=True)
    return df


def get_filename(filepath: str):
    filename = re.findall(r'[^\\/:*?"<>|\r\n]+$', filepath)[0].split('.')[0]
    return filename


def get_folder(filepath: str):
    folder_path = "/".join(filepath.split("/")[:-1]) + "/"
    return folder_path


def format_time(_formatter="%m-%d-%H-%M-%S"):
    return datetime.now().strftime(_formatter)
