from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import numpy

scaler = MinMaxScaler(feature_range=(0, 1))
model = Sequential()


def normalize(dataset):
    dataset = get_scaler_format(dataset)
    dataset = scaler.fit_transform(dataset)
    return get_scaler_unformat(dataset)


def unnormalize(result):
    return scaler.inverse_transform(result)


def get_scaler_format(dataset):
    return list(map(lambda x: [x], dataset))


def get_scaler_unformat(dataset):
    return list(map(lambda x: x[0], dataset))


def train(trainX, trainY, epochs, look_back):
    model.add(LSTM(4, input_shape=(1, look_back)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=epochs, batch_size=1, verbose=2)


def get(sequence, look_back):
    dataset = normalize(sequence)
    dataset = create_input(dataset, look_back, False)
    dataset = numpy.reshape(dataset, (dataset.shape[0], 1, dataset.shape[1]))
    predict = model.predict(dataset)
    return get_scaler_unformat(unnormalize(predict))


def train_sequence(sequence, epochs, look_back):
    sequence = normalize(sequence)
    trainX = create_input(sequence, look_back, True)
    trainY = create_output(sequence, look_back)
    trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    train(trainX, trainY, epochs, look_back)


def create_input(sequence, look_back, train=False):
    data = []
    for i in range(len(sequence)-look_back+1):
        value = sequence[i:i+look_back]
        data.append(value)
    data = numpy.array(data)
    return data[:-1] if train else data


def create_output(sequence, look_back):
    data = sequence[look_back:]
    return numpy.array(data)
