from datetime import datetime
import config


def get_month():
    current_month = datetime.now().month
    month_initials = config.get()["market"]["month_initials"]
    return month_initials[current_month]


def get_initials():
    return config.get()["market"]["initials"]


def get_year():
    return datetime.now().year


def get_complete_initials():
    return str(get_initials()) + str(get_month()) + str(get_year())[-2:]


def get_current_period():
    initials_period = config.get()["market"]["initials_period"]
    return initials_period[get_month()]


def get_start_date_period():
    period = get_current_period()
    return datetime(datetime.now().year, period["start_at"]["month"], period["start_at"]["day"])
