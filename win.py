from datetime import datetime
import config

month_initials = config.get()["market"]["month_initials"]

initials = "WIN"


def get_month():
    current_month = datetime.now().month
    return month_initials[current_month]


def get_initials():
    return initials


def get_year():
    current_year = datetime.now().year
    return current_year


def get_complete_initials():
    return str(get_initials()) + str(get_month()) + str(get_year())[-2:]


def get_current_period():
    initials_period = config.get()["market"]["initials_period"]
    return initials_period[get_month()]


def get_start_date_period():
    period = get_current_period()
    return datetime(datetime.now().year, period["start_at"]["month"], period["start_at"]["day"])
