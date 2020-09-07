import win
import market
import predictor
import config
import sys
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def execute():
    look_back = config.get()["predictor"]['look_back']
    look_beyond = config.get()["predictor"]['look_beyond']
    date = datetime.now()

    start_date = win.get_start_date_period()
    end_date = datetime(date.year, date.month, date.day) + timedelta(days=1)
    initials = win.get_complete_initials()

    rates = market.get_rates_from_date(initials, start_date, end_date)
    sequence = list(map(lambda val: val['close'], rates))

    predictor.load()
    predict = predictor.forecast(sequence, look_back, look_beyond)

    plt.plot(predict, label='Predict')
    plt.plot(sequence, label='Real')
    plt.legend()
    plt.show()
