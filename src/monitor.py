import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# Lista de ativos (assets)
ASSETS = [
    "PETR4.SA",
]

FILE_NAME = "cotacoes_historicas.csv"

def fetch_and_save_data():
    """Busca as cotações atuais e as salva em arquivo csv."""
    print(f"[{datetime.now().strftime('%H:%M:&S')}] Iniciando coleta de dados.")
    # 1. Coleta os dados com yfinance
    data = yf.download(ASSETS, period="1d",interval="1m")

    # trata falha na coleta de dados
    if data.empty:
        print("Falha ao coletar dados.")
        return

    # 2. Processamento com Pandas
    last_close = data['Close'].iloc[-1]
    new_data = pd.DataFrame({ASSETS[0]: [last_close]})
    
    new_data['Timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # coluna para registrar data/hora da coleta
    new_data = new_data[['Timestamp'] + [col for col in new_data.columns if col != 'Timestamp']]

    # 3. Persistência (Salvamento no CSV)
    
    if os.path.exists(FILE_NAME):
        # Se o arquivo existe, anexa sem o cabeçalho
        new_data.to_csv(FILE_NAME, mode='a', header=False, index=False)
        print(f"Dados anexados a {FILE_NAME}")
    else:
        # Se o arquivo não existe, cria com o cabeçalho
        new_data.to_csv(FILE_NAME, mode='w', header=True, index=False)
        print(f"Novo arquivo {FILE_NAME} criado com sucesso.")

    print("-" * 20)

if __name__ == "__main__":
    # Exemplo de execução única para teste
    fetch_and_save_data()