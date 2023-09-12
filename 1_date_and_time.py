from datetime import datetime, date, timedelta
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    dt_now = date.today()
    delta = timedelta(days=1)
    dt_yesterday = dt_now - delta
    delta = timedelta(days=30)
    dt_30 = dt_now - delta
    print(f"Вчера: {dt_yesterday}")
    print(f"Сегодня: {dt_now}")
    print(f"30 дней назад: {dt_30}")


def str_2_datetime(date_string):
    date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
