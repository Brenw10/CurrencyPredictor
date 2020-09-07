import win
import market
import predictor
import config
from datetime import datetime, timedelta


def execute():
    look_back = config.get()["predictor"]['look_back']
    epochs = config.get()["predictor"]['epochs']
    date = datetime.now()

    start_date = win.get_start_date_period()
    end_date = datetime(date.year, date.month, date.day) + timedelta(days=1)
    initials = win.get_complete_initials()

    rates = market.get_rates_from_date(initials, start_date, end_date)
    sequence = list(map(lambda val: val['close'], rates))

    predictor.train_sequence(sequence, epochs, look_back)

    predictor.save()