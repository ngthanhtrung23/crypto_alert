from datetime import datetime


def current_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


def timestamp_to_str(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%y-%m-%d - %H:%M:%S")
