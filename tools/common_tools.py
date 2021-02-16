import datetime


def convert_time(date):
    time_str = datetime.datetime.strftime(date,"%Y-%m-%d %H:%M:%S")
    return time_str