# import win
# import market
import arrayutils
# import tutorial
import predictor
# import numpy
# from datetime import datetime
import matplotlib.pyplot as plt

# start_date = win.get_start_date_period()
# initials = win.get_complete_initials()

# rates = market.get_rates_from_start_date(initials, start_date)
# # rates = market.get_rates_from_start_date(initials, datetime(2020, 8, 31, 11))
# dataset = list(map(lambda val: [val['close']], rates))
# train = predictor.normalize(dataset)

# look_back = 1
# trainX, trainY = tutorial.create_dataset(train, look_back)
# trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))

# predictor.train(trainX, trainY, 100, look_back)
# result = predictor.get(trainX)

# future = result.reshape(1, -1)[0]
# for i in range(100):
#     p = numpy.array(list(map(lambda val: [val], future)))
#     p = numpy.reshape(p, (p.shape[0], 1, p.shape[1]))
#     predict = predictor.get(p)
#     last = predict[len(predict) - 1]
#     future = numpy.append(future, last)

# future = numpy.array(list(map(lambda val: [val], future)))

# plt.plot(dataset)
# plt.plot(predictor.unnormalize(result))
# plt.plot(predictor.unnormalize(future))
# plt.show()

look_back = 5
epochs = 500
sequence = [10, 20, 30, 40, 50, 30, 40, 50, 60, 70, 50, 60, 70, 80, 90]
next_sequence = [70, 80, 90, 100, 110, 90]

diff_sequence = arrayutils.get_vector_diffs(sequence)
diff_next_sequence = arrayutils.get_vector_diffs(sequence + next_sequence)

predictor.train_sequence(diff_sequence, epochs, look_back)
predict = predictor.get(diff_next_sequence, look_back)

unpredictable = predictor.get_scaler_format(diff_sequence[:look_back])
predict = unpredictable + predict.tolist()

plt.plot(predict)
plt.plot(diff_sequence)
plt.show()
