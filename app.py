import time
import win
import market
import predictor
import config
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

start_time = time.time()

look_back = config.get()["predictor"]['look_back']
look_beyond = config.get()["predictor"]['look_beyond']
epochs = config.get()["predictor"]['epochs']
train_size = 1 - config.get()["predictor"]['train_size']

date = datetime.now()
start_date = win.get_start_date_period()
end_date = datetime(date.year, date.month, date.day) + timedelta(days=1)
initials = win.get_complete_initials()

rates = market.get_rates_from_date(initials, start_date, end_date)
sequence = list(map(lambda val: val['close'], rates))

predictor.train_sequence(sequence[int(len(sequence) * train_size):], epochs, look_back)
predict = predictor.forecast(sequence, look_back, look_beyond)

print("--- %s seconds ---" % (time.time() - start_time))
plt.plot(sequence + predict[len(sequence):], label='Forecast')
plt.plot(predict[:len(sequence)], label='Predict')
plt.plot(sequence, label='Real')
plt.legend()
plt.show()