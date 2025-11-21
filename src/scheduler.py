import time
import schedule
from datetime import datetime
from monitor import fetch_and_save_data

def safe_fetch_and_save():
    """
    Função wrapper que chama 'fetch_and_save_data' e lida com exceções
    para garantir que o scheduler não pare.
    """
    try:
        fetch_and_save_data()
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ocorreu um erro: {e}")

def run_scheduler():
    """Configura e inicia o loop de agendamento."""

    # Agenda a tarefa usando a função wrapper segura
    schedule.every(10).minutes.do(safe_fetch_and_save)

    # Execução imediata ao iniciar
    print("Executando a primeira coleta de dados...")
    safe_fetch_and_save()

    print("Scheduler iniciado. Próxima coleta em 10 minutos...")

    # Loop principal que verifica e executa as tarefas agendadas
    while True:
        schedule.run_pending()
        time.sleep(1) # Aguarda um segundo antes de verificar novamente

if __name__ == "__main__":
    run_scheduler()