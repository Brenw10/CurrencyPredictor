import win
import market
import arrayutils
import tutorial

start_date = win.get_start_date_period()
initials = win.get_complete_initials()

rates = market.get_rates_from_start_date(initials, start_date)
dataset = list(map(lambda val: val['close'], rates))
# dataset = arrayutils.get_vector_diffs(dataset)

# train_size = int(len(dataset) * 0.67)
# test_size = len(dataset) - train_size
# train, test = dataset[:train_size], dataset[train_size:]

# trainX, trainY = train[1:], train[:len(train)-1]
# testX, testY = test[1:], test[:len(train)-1]


dataset = list(map(lambda val: [val], dataset))
print(len(dataset))
tutorial.main(dataset, 1, 300)
