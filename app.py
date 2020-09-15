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
train_size = config.get()["predictor"]['train_size']


def get_sequence():
    start_date = win.get_start_date_period()
    end_date = datetime(date.year, date.month, date.day) + timedelta(days=1)
    initials = win.get_complete_initials()

    rates = market.get_rates_from_date(initials, start_date, end_date)
    return list(map(lambda val: val['close'], rates))


def train():
    sequence = get_sequence()
    start_at = len(sequence) - train_size
    predictor.train_sequence(sequence[start_at:], epochs, look_back)


def predict():
    sequence = get_sequence()
    real_predict = predictor.get(sequence, look_back)
    forecast_predict = predictor.forecast(sequence, look_back, look_beyond)

    plt.plot(sequence + forecast_predict, label='Forecast')
    plt.plot(real_predict, label='Predict')
    plt.plot(sequence, label='Real')
    plt.legend()
    plt.show()

    predict()


train()
predict()
