import numpy as np
import pandas as pd

def calcular_duty_cycle(sinal):
    # Contar o número total de pontos no sinal (período total)
    periodo_total = len(sinal)
    
    # Contar o número de amostras em que o sinal está em nível alto (1)
    tempo_alto = sum(sinal)
    
    # Calcular o duty cycle como porcentagem
    duty_cycle = (tempo_alto / periodo_total) * 100
    return duty_cycle

duty_cycle = calcular_duty_cycle(sinal)
print(f"Duty Cycle: {duty_cycle:.2f}%")