from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

scaler = MinMaxScaler(feature_range=(0, 1))
model = Sequential()


def normalize(dataset):
    return scaler.fit_transform(dataset)


def unnormalize(result):
    return scaler.inverse_transform(result)


def train(trainX, trainY, epochs, look_back=1):
    model.add(LSTM(4, input_shape=(1, look_back)))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, epochs=epochs, batch_size=1, verbose=2)


def get(dataset, unnorm=False):
    predict = model.predict(dataset)
    return unnormalize(predict) if unnorm else predict
