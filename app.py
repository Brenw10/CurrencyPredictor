import win
import market
import arrayutils
import predictor
import matplotlib.pyplot as plt
from datetime import datetime

start_date = win.get_start_date_period()
initials = win.get_complete_initials()

rates = market.get_rates_from_start_date(initials, datetime(2020, 9, 4))
# rates = market.get_rates_from_start_date(initials, start_date)

look_back = 2
look_beyond = 5
epochs = 500
sequence = [10, 20, 30, 50, 60, 70, 90, 100, 110]
# sequence = list(map(lambda val: val['close'], rates))

predictor.train_sequence(sequence, epochs, look_back)
predict = predictor.forecast(sequence, look_back, look_beyond)

plt.plot(predict)
plt.plot(sequence)
plt.show()
