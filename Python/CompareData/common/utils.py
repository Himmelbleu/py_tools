import builtins
import re
from datetime import datetime


def reserve(number, decimal_places=2):
    result = builtins.round(number, decimal_places)
    return int(result) if result.is_integer() else result


def percent_rate(_numerator, _denominator):
    if _denominator != 0:
        return (_numerator / _denominator) * 100
    else:
        return 0


def get_num(_text):
    match = re.search(r'[-+]?\d+', str(_text))
    if match:
        return float(match.group(0))
    return 0


def format_time(_formatter="%m-%d-%H-%M-%S"):
    return datetime.now().strftime(_formatter)
