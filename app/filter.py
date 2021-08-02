from datetime import datetime


def format_datetime(value: datetime, fmt='%Y년 %m월 %d일 %H:%M'):
    return value.strftime(fmt)
