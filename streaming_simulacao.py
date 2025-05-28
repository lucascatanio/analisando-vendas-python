import random
import time
from datetime import datetime

LIMITE = 70  # Temperatura limite
arquivo_alertas = "alertas.txt"

def gerar_dado_sensor():
    return random.uniform(50, 90)  # Gera temperatura aleatória

with open(arquivo_alertas, 'w') as f:
    f.write('=== Alertas de Temperatura ===\n')

print("Iniciando simulação de streaming... (Ctrl+C para parar)")

try:
    while True:
        temp = gerar_dado_sensor()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{timestamp}] Temperatura: {temp:.2f}°C")

        if temp > LIMITE:
            alerta = f"[{timestamp}] ALERTA! Temperatura alta: {temp:.2f}°C\n"
            print(alerta)
            with open(arquivo_alertas, 'a') as f:
                f.write(alerta)

        time.sleep(2)  # Simula chegada de dados a cada 2 segundos
except KeyboardInterrupt:
    print("Simulação encerrada.")
