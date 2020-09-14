import win
import market
import predictor
import config
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

date = datetime.now()
look_back = config.get()["predictor"]['look_back']
look_beyond = config.get()["predictor"]['look_beyond']
epochs = config.get()["predictor"]['epochs']
train_size = 1 - config.get()["predictor"]['train_size']


def get_sequence():
    start_date = win.get_start_date_period()
    end_date = datetime(date.year, date.month, date.day) + timedelta(days=1)
    initials = win.get_complete_initials()

    rates = market.get_rates_from_date(initials, start_date, end_date)
    return list(map(lambda val: val['close'], rates))


def train():
    sequence = get_sequence()
    size = int(len(sequence) * train_size)
    predictor.train_sequence(sequence[size:], epochs, look_back)


def predict():
    sequence = get_sequence()
    result = predictor.forecast(sequence, look_back, look_beyond)

    plt.plot(sequence + result[len(sequence):], label='Forecast')
    plt.plot(result[:len(sequence)], label='Predict')
    plt.plot(sequence, label='Real')
    plt.legend()
    plt.show()

    predict()


train()
predict()
