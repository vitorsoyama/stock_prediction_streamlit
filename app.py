import streamlit as st
import sys
sys.path.append('tickers_data')
sys.path.append('model')
import get_tickers as gt
import model_and_prediction as mp


# Lista de alguns tickers da B3
TICKERS_B3 = gt.get_b3_tickers_from_file("tickers_data/statusinvest-busca-avancada.csv")

# Função para carregar dados de ações brasileiras
# Interface Streamlit
st.set_page_config(page_title='Previsão de Ações B3', layout='wide')
st.title('Previsão de Ações da B3 com IA')

# Dropdown para seleção de ticker
ticker = st.selectbox('Selecione a ação', TICKERS_B3)

if st.button('Carregar e Prever'):
    data = mp.load_data(ticker)
    if data.empty:
        st.error('Ticker não encontrado ou sem dados.')
    else:
        st.subheader(f'Dados recentes de {ticker}.SA')
        st.write(data.tail(5))
        em_andamento = st.subheader('Previsão em andamento aguarde...')

        X_train, X_test, y_train, y_test, scaler = mp.prepare_data(data)
        model = mp.build_and_train(X_train, y_train)
        prediction = mp.predict(model, data, scaler)

        em_andamento = em_andamento.empty()

        st.subheader(f'Preço previsto de fechamento para o próximo pregão: R$ {prediction:.2f}')
        st.subheader(f'Com um erro médio (RMSE) de: R$ {model.evaluate(X_test, y_test, batch_size=128)[0]:.2f}')
        st.line_chart(data.set_index('Date')['Close'], y = "Close")