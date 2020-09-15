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
real_size = config.get()["predictor"]['real_size']


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
    forecast_predict = predictor.forecast(sequence, look_back, look_beyond)

    show_sequence = sequence[len(sequence) - real_size:]
    plt.plot(show_sequence + forecast_predict, label='Forecast', color='blue')
    plt.plot(show_sequence, label='Real', color='green')
    plt.legend()
    plt.show()

    predict()


train()
predict()
