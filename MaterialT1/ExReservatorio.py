# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 11:53:46 2026

@author: joisa
"""

import math

def volume_cilindro(raio, altura):
    """Calcula o volume total de um cilindro: V = π * r² * h"""
    return math.pi * (raio ** 2) * altura


def volume_perdido(raio, altura, espessura):
    """Calcula o volume perdido devido ao revestimento: V = (2πrh + πr²) * e"""
    area_revestida = (2 * math.pi * raio * altura) + (math.pi * raio ** 2)
    return area_revestida * espessura


def volume_util(raio, altura, tipo_revestimento):
    """Calcula o volume útil do reservatório considerando o tipo de revestimento"""
    # Define a espessura de acordo com o tipo de revestimento
    if tipo_revestimento == 'epoxi':
        espessura = 0.003
    elif tipo_revestimento == 'fibra_vidro':
        espessura = 0.005
    elif tipo_revestimento == 'azulejo':
        espessura = 0.007
    else:
        espessura = 0.0
    
    volume_total = volume_cilindro(raio, altura)
    perdido = volume_perdido(raio, altura, espessura)
    
    return volume_total - perdido


# Programa Principal
print("=== DADOS DO RESERVATÓRIO 1 ===")
raio1 = float(input("Raio do reservatório 1 (m): "))
altura1 = float(input("Altura do reservatório 1 (m): "))
revest1 = input("Tipo de revestimento (epoxi/fibra_vidro/azulejo/outro): ").lower()

print("\n=== DADOS DO RESERVATÓRIO 2 ===")
raio2 = float(input("Raio do reservatório 2 (m): "))
altura2 = float(input("Altura do reservatório 2 (m): "))
revest2 = input("Tipo de revestimento (epoxi/fibra_vidro/azulejo/outro): ").lower()

# Calcula os volumes úteis
vol1 = volume_util(raio1, altura1, revest1)
vol2 = volume_util(raio2, altura2, revest2)

print("\n=== RESULTADO ===")
print(f"Reservatório 1 - Volume útil: {vol1:.2f} m³")
print(f"Reservatório 2 - Volume útil: {vol2:.2f} m³")

# Comparação
if vol1 > vol2:
    print("Reservatório 1 tem maior volume útil")
elif vol2 > vol1:
    print("Reservatório 2 tem maior volume útil")
else:
    print("Os dois reservatórios têm o mesmo volume útil")