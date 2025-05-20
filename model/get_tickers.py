def get_b3_tickers_from_file(file_path="tickers_b3.txt"):
    """
    Lê uma lista de tickers da B3 de um arquivo de texto,
    onde cada linha contém um ticker (ex: PETR4.SA).

    Args:
        file_path (str): O caminho para o arquivo de texto.

    Returns:
        list: Uma lista de strings contendo os tickers.
        Retorna uma lista vazia se o arquivo não for encontrado ou estiver vazio.
    """
    tickers = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                # Remove espaços em branco e quebras de linha
                ticker = line.strip()
                if ticker: # Adiciona apenas se a linha não estiver vazia
                    tickers.append(ticker)
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_path}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

    tickers = tickers[1::]

    return tickers
