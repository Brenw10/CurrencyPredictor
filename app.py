import win
import market
import arrayutils
from functools import reduce
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

start_date = win.get_start_date_period()
initials = win.get_complete_initials()
look_back = 1

rates = market.get_rates_from_start_date(initials, start_date)
closes = list(map(lambda val: val['close'], rates))
dataset = arrayutils.get_diffs(closes)

train_size = int(len(dataset) * 0.67)
test_size = len(dataset) - train_size

train, test = dataset[:train_size], dataset[train_size:]

trainX, trainY = train[:len(train)], train[1:]
testX, testY = test[:len(train)], test[1:]

model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=100, batch_size=1, verbose=2)
