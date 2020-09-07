import win
import market
import arrayutils
import predictor
import matplotlib.pyplot as plt
from datetime import datetime

look_back = 1
look_beyond = 200
epochs = 1

start_date = win.get_start_date_period()
initials = win.get_complete_initials()

rates = market.get_rates_from_start_date(initials, datetime(2020, 9, 4))
sequence = list(map(lambda val: val['close'], rates))

predictor.train_sequence(sequence, epochs, look_back)
predict = predictor.forecast(sequence, look_back, look_beyond)

print(sequence)
print(predict)

plt.plot(predict)
plt.plot(sequence)
plt.show()
