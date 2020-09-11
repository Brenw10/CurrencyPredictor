from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.models import load_model
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


def reshape(dataset):
    return numpy.reshape(dataset, (dataset.shape[0], 1, dataset.shape[1]))


def train(trainX, trainY, epochs, look_back):
    model.add(LSTM(1, input_shape=(1, look_back)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=epochs, batch_size=1, verbose=2)


def get(sequence, look_back):
    dataset = normalize(sequence)
    dataset = create_input(dataset, look_back, False)
    dataset = reshape(dataset)
    predict = model.predict(dataset)
    predict = unnormalize(predict)
    predict = get_scaler_unformat(predict)
    return sequence[:look_back] + predict


def forecast(sequence, look_back, look_beyond):
    dataset = get(sequence, look_back)
    for _ in range(look_beyond-1):
        to_predict = dataset[len(dataset)-look_back:]
        predict = get(to_predict, look_back)
        last_predict = predict[len(predict)-1]
        dataset.append(last_predict)
    return dataset


def train_sequence(sequence, epochs, look_back):
    sequence = normalize(sequence)
    trainX = create_input(sequence, look_back, True)
    trainY = create_output(sequence, look_back)
    trainX = reshape(trainX)
    train(trainX, trainY, epochs, look_back)


def create_input(sequence, look_back, is_train=False):
    data = []
    for i in range(len(sequence)-look_back+1):
        value = sequence[i:i+look_back]
        data.append(value)
    data = numpy.array(data)
    return data[:-1] if is_train else data


def create_output(sequence, look_back):
    data = sequence[look_back:]
    return numpy.array(data)
