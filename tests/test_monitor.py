import os
import pandas as pd
from unittest.mock import patch, MagicMock
from datetime import datetime

from src.monitor import fetch_and_save_data

# Fixture para dados de exemplo que seriam retornados pelo yfinance
def mock_yfinance_download():
    """Cria um DataFrame do pandas de exemplo para simular a resposta da API."""
    data = {
        'Close': [150.0],
        'Open': [149.0],
        'High': [151.0],
        'Low': [148.0],
        'Volume': [1000000]
    }
    index = pd.to_datetime(['2025-11-21 10:30:00'])
    df = pd.DataFrame(data, index=index)
    # yfinance pode retornar um MultiIndex para as colunas, vamos simular isso
    df.columns = pd.MultiIndex.from_product([['Close', 'Open', 'High', 'Low', 'Volume'], ['PETR4.SA']])
    # O código acessa apenas 'Close', então vamos simplificar para o que o código espera
    df = df[['Close']]
    df.columns = df.columns.droplevel(1)
    return df

@patch('src.monitor.yf.download')
@patch('src.monitor.datetime')
def test_fetch_and_save_data_creates_new_file(mock_dt, mock_download, tmp_path):
    """
    Testa se um novo arquivo CSV é criado quando nenhum existe.
    """
    # Configuração do Mock
    mock_download.return_value = mock_yfinance_download()
    mock_dt.now.return_value = datetime(2025, 11, 21, 10, 31, 0)
    
    # Define o caminho do arquivo de saída para o diretório temporário
    file_path = tmp_path / "cotacoes.csv"
    
    # Sobrescreve a variável global FILE_NAME dentro do escopo do teste
    with patch('src.monitor.FILE_NAME', file_path):
        fetch_and_save_data()

    # Verificações
    assert os.path.exists(file_path)
    
    df = pd.read_csv(file_path)
    assert len(df) == 1
    assert df.iloc[0]['Timestamp'] == '2025-11-21 10:31:00'
    assert df.iloc[0]['PETR4.SA'] == 150.0
    assert list(df.columns) == ['Timestamp', 'PETR4.SA']


@patch('src.monitor.yf.download')
def test_fetch_and_save_data_appends_to_existing_file(mock_download, tmp_path):
    """
    Testa se os dados são anexados a um arquivo CSV existente.
    """
    # Configuração do Mock
    mock_download.return_value = mock_yfinance_download()
    
    file_path = tmp_path / "cotacoes.csv"

    with patch('src.monitor.FILE_NAME', file_path):
        # Primeira chamada para criar o arquivo
        with patch('src.monitor.datetime') as mock_dt1:
            mock_dt1.now.return_value = datetime(2025, 11, 21, 10, 31, 0)
            fetch_and_save_data()

        # Segunda chamada para anexar ao arquivo
        with patch('src.monitor.datetime') as mock_dt2:
            mock_dt2.now.return_value = datetime(2025, 11, 21, 10, 41, 0)
            fetch_and_save_data()

    # Verificações
    df = pd.read_csv(file_path)
    assert len(df) == 2
    assert df.iloc[0]['Timestamp'] == '2025-11-21 10:31:00'
    assert df.iloc[1]['Timestamp'] == '2025-11-21 10:41:00'
    assert df.iloc[1]['PETR4.SA'] == 150.0

@patch('src.monitor.yf.download')
def test_fetch_and_save_data_handles_api_failure(mock_download, tmp_path, capsys):
    """
    Testa se o sistema lida corretamente com uma falha na API (DataFrame vazio).
    """
    # Configuração do Mock para falha
    mock_download.return_value = pd.DataFrame()
    
    file_path = tmp_path / "cotacoes.csv"

    with patch('src.monitor.FILE_NAME', file_path):
        fetch_and_save_data()

    # Verificações
    assert not os.path.exists(file_path)
    captured = capsys.readouterr()
    assert "Falha ao coletar dados." in captured.out

