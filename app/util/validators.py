

from datetime import datetime


def string_to_date(date):
    date_time_obj_fromdate = datetime.strptime(date, '%Y-%m-%d')
    return date_time_obj_fromdate