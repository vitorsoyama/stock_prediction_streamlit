import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
import tensorflow.keras as keras
import streamlit as st

@st.cache_data
def load_data(ticker):
    full_ticker = ticker + ".SA"
    data = yf.download(full_ticker, period='5y')
    data.reset_index(inplace=True)
    data.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
    return data

# Função para preparar dados para o modelo
def prepare_data(data):
    scaler = MinMaxScaler(feature_range=(0, 1))
    close_prices = data['Close'].values.reshape(-1, 1)
    scaled = scaler.fit_transform(close_prices)

    X, y = [], []
    for i in range(60, len(scaled)):
        X.append(scaled[i-60:i, 0])
        y.append(scaled[i, 0])
    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Divisão treino/teste: 80% treino, 20% teste
    split = int(len(X) * 0.8)
    X_train, X_test = X[:split], X[split:]
    y_train, y_test = y[:split], y[split:]

    return X_train, X_test, y_train, y_test, scaler

# Função para construir e treinar o modelo
def build_and_train(X_train, y_train):
    model = Sequential()
    model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(LSTM(50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error', metrics = [keras.metrics.RootMeanSquaredError()])
    model.fit(X_train, y_train, epochs=5, batch_size=32)
    return model


# Função para fazer previsões
def predict(model, data, scaler):
    inputs = data['Close'].values[-60:].reshape(-1, 1)
    inputs = scaler.transform(inputs)
    X_test = np.array([inputs[:, 0]]).reshape((1, 60, 1))
    pred = model.predict(X_test)
    return scaler.inverse_transform(pred)[0][0]

