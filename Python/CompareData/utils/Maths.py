import builtins
import re

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
