# Python Asset Tracker

A simple and efficient script to monitor and log historical stock prices for specified assets using Python. This project fetches data periodically from the yfinance API, processes it with pandas, and saves it to a CSV file.

---

## Features

- **Automated Data Fetching**: Runs automatically at a set interval using a scheduler.
- **Historical Logging**: Appends new data to a CSV file, creating a historical record of asset prices.
- **Robust Error Handling**: Ensures the scheduler continues to run even if an API call fails.
- **Professional Testing**: Includes a full test suite using `pytest` to ensure reliability and correctness.
- **Easy to Configure**: Simply add or remove asset tickers from the list in `src/monitor.py`.

## Getting Started

### Prerequisites

- Python 3.9+
- `venv` module for virtual environments

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/metzker87/python-asset-tracker.git
    cd python-asset-tracker
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Scheduler

To start the monitoring script, run the scheduler from the root directory of the project:

```bash
python src/scheduler.py
```

The script will immediately fetch the first data point and then run every 10 minutes to log the latest asset prices.

### Running Tests

To run the test suite and verify the application's functionality, use `pytest`:

```bash
pytest
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
---

# Português (BR)

## Python Asset Tracker

Um script simples e eficiente para monitorar e registrar o histórico de cotações de ativos especificados usando Python. Este projeto busca dados periodicamente da API do yfinance, os processa com pandas e os salva em um arquivo CSV.

## Recursos

- **Coleta de Dados Automatizada**: Executa automaticamente em um intervalo definido usando um agendador.
- **Registro Histórico**: Anexa novos dados a um arquivo CSV, criando um registro histórico dos preços dos ativos.
- **Tratamento de Erros Robusto**: Garante que o agendador continue em execução mesmo que uma chamada de API falhe.
- **Testes Profissionais**: Inclui uma suíte de testes completa usando `pytest` para garantir confiabilidade e correção.
- **Fácil de Configurar**: Basta adicionar ou remover os tickers dos ativos da lista em `src/monitor.py`.

## Como Começar

### Pré-requisitos

- Python 3.9+
- Módulo `venv` para ambientes virtuais

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/metzker87/python-asset-tracker.git
    cd python-asset-tracker
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

### Executando o Agendador

Para iniciar o script de monitoramento, execute o agendador a partir do diretório raiz do projeto:

```bash
python src/scheduler.py
```

O script buscará imediatamente o primeiro ponto de dados e, em seguida, será executado a cada 10 minutos para registrar as cotações mais recentes dos ativos.

### Executando os Testes

Para executar a suíte de testes e verificar a funcionalidade da aplicação, use `pytest`:

```bash
pytest
```

---

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
