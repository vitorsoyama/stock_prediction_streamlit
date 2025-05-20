# Previsão de Ações B3 com IA

Este projeto oferece uma **interface interativa** para previsão de preços de ações da B3 (Bolsa de Valores do Brasil) utilizando **inteligência artificial**. Desenvolvido com **Streamlit**, ele permite que você selecione um ticker de ação e visualize a previsão de fechamento para o próximo pregão, juntamente com o histórico de preços.

## Funcionalidades

* **Seleção de Ticker**: Escolha qualquer ação listada na B3 através de um menu suspenso.
* **Visualização de Dados Recentes**: Veja os últimos 5 dias de dados de fechamento da ação selecionada.
* **Previsão de Preço**: Obtenha uma previsão do preço de fechamento para o próximo dia de negociação.
* **Avaliação do Modelo**: Verifique o erro médio (RMSE) do modelo de previsão.
* **Gráfico Interativo**: Visualize o histórico de preços de fechamento da ação.

## Como Usar

1.  **Execute o aplicativo Streamlit**:

    ```bash
    streamlit run app.py
    ```

    (Substitua `app.py` pelo nome do arquivo principal do seu projeto.)

2.  **Selecione uma Ação**: No menu suspenso "**Selecione a ação**", escolha o ticker da empresa que você deseja analisar.
3.  **Carregar e Prever**: Clique no botão "**Carregar e Prever**" para que o aplicativo carregue os dados, treine o modelo e exiba a previsão.

---

## Estrutura do Projeto

O projeto é organizado nos seguintes arquivos e diretórios:

* `main.py`: O arquivo principal do Streamlit que orquestra a interface do usuário. Ele importa funções dos outros módulos para carregar tickers, obter dados de ações, preparar os dados, construir e treinar o modelo, e fazer a previsão. É o ponto de entrada para executar a aplicação web.
* `tickers_data/`: Este diretório deve conter o arquivo com a lista de tickers da B3.
    * `statusinvest-busca-avancada.csv`: O arquivo CSV que contém a lista de tickers utilizada pelo módulo `get_tickers`.
* `model/`: Este diretório contém os módulos Python responsáveis pela lógica de dados e modelagem de IA.
    * `get_tickers.py`: Contém a função `get_b3_tickers_from_file` que lê a lista de tickers de um arquivo especificado.
    * `model_and_prediction.py`: Contém as funções para baixar dados de ações (`load_data`), preparar os dados para o modelo (`prepare_data`), construir e treinar o modelo LSTM (`build_and_train`), e realizar a previsão (`predict`).

## Tecnologias Utilizadas

* **Streamlit**: Para a criação da interface web interativa.
* **Pandas**: Para manipulação e análise de dados.
* **Numpy**: Para operações numéricas eficientes.
* **TensorFlow/Keras**: Para a construção e treinamento do modelo de aprendizado de máquina (redes neurais LSTM).
* **Scikit-learn**: Para pré-processamento de dados (e.g., MinMaxScaler).
* **yfinance**: Para baixar dados históricos de ações.

## Instalação

Para rodar este projeto, você precisará ter as seguintes bibliotecas Python instaladas. Recomenda-se usar um ambiente virtual.

Você pode instalar as dependências usando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt

O conteúdo do arquivo requirements.txt é:

streamlit
pandas
numpy
tensorflow
scikit-learn
yfinance

Certifique-se também de que o arquivo CSV com a lista de tickers (statusinvest-busca-avancada.csv) esteja presente no diretório tickers_data/ e que o caminho no arquivo main.py esteja correto.