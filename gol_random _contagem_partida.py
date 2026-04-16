# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:46:59 2026

@author: PC37
"""

import random

def exibeJogos(g1,g2,g3,g4,g5,g6,a1,a2,a3,a4,a5,a6):
    soma_vit=0
    soma_gol = g1+g2+g3+g4+g5+g6
    soma_contra = a1+a2+a3+a4+a5+a6
    print("---Partida 1---")
    if g1 > a1:
        resultado = "OLIMPO VENCEU!"
        soma_vit+=1
    elif g1 < a1:
        resultado = "OLIMPO PERDEU!"
    else:
        resultado = "EMPATE!"
    print(f"OLIMPO ({g1}) X Adv1 ({a1}): {resultado}")
    print()
    print("---Partida 2---")
    if g2 > a2:
        resultado = "OLIMPO VENCEU!"
        soma_vit+=1
    elif g2 < a2:
        resultado = "OLIMPO PERDEU!"
    else:
        resultado = "EMPATE!"
    print(f"OLIMPO ({g2}) X Adv2 ({a2}): {resultado}")
    print()
    print("---Partida 3---")
    if g3 > a3:
        resultado = "OLIMPO VENCEU!"
        soma_vit+=1
    elif g3 < a3:
        resultado = "OLIMPO PERDEU!"
    else:
        resultado = "EMPATE!"
    print(f"OLIMPO ({g3}) X Adv3 ({a3}): {resultado}")
    print()
    print("---Partida 4---")
    if g4 > a4:
        resultado = "OLIMPO VENCEU!"
        soma_vit+=1
    elif g4 < a4:
        resultado = "OLIMPO PERDEU!"
    else:
        resultado = "EMPATE!"
    print(f"OLIMPO ({g4}) X Adv4 ({a4}): {resultado}")
    print()
    print("---Partida 5---")
    if g5 > a5:
        resultado = "OLIMPO VENCEU!"
        soma_vit+=1
    elif g5 < a5:
        resultado = "OLIMPO PERDEU!"
    else:
        resultado = "EMPATE!"
    print(f"OLIMPO ({g5}) X Adv5 ({a5}): {resultado}")
    print()
    print("---Partida 6---")
    if g6 > a6:
        resultado = "OLIMPO VENCEU!"
        soma_vit+=1
    elif g6 < a6:
        resultado = "OLIMPO PERDEU!"
    else:
        resultado = "EMPATE!"
    print(f"OLIMPO ({g6}) X Adv6 ({a6}): {resultado}")
    print()
    print(f"Vitorias: {soma_vit} - Gols: {soma_gol} - Gols sofridos: {soma_contra}")





g1 = random.randint(0,7)
g2 = random.randint(0,7)
g3 = random.randint(0,7)
g4 = random.randint(0,7)
g5 = random.randint(0,7)
g6 = random.randint(0,7)
a1 = random.randint(0,7)
a2 = random.randint(0,7)
a3 = random.randint(0,7)
a4 = random.randint(0,7)
a5 = random.randint(0,7)
a6 = random.randint(0,7)

exibeJogos(g1,g2,g3,g4,g5,g6,a1,a2,a3,a4,a5,a6)


print()
print()
print()
def exibeJogosGemini():
    soma_vitorias = 0
    soma_gol_OLIMPO = 0
    soma_contra_OLIMPO = 0
    for i in range(1, 7):
        # Gera os gols da partida ATUAL sorteada
        gols_olimpo = random.randint(0, 7)
        gols_adv = random.randint(0, 7)
        # Acumula os gols totais
        soma_gol_OLIMPO = soma_gol_OLIMPO + gols_olimpo
        soma_contra_OLIMPO = soma_contra_OLIMPO + gols_adv
        
        # Lógica de vitória/derrota da partida atual
        if gols_olimpo > gols_adv:
            resultado = "OLIMPO venceu!"
            soma_vitorias += 1
        elif gols_olimpo < gols_adv:
            resultado = "OLIMPO perdeu!"
        else:
            resultado = "EMPATE!"
            
        # O 'i' serve para mostrar o número do adversário (Adv1, Adv2...)
        print(f"OLIMPO ({gols_olimpo}) X Adv{i} ({gols_adv}): {resultado}")
        
    # Depois que o 'for' acabar as 6 rodadas, imprime o resumo final
    print(f"Vitorias:{soma_vitorias} - Gols feitos:{soma_gol_OLIMPO} - Gols sofridos:{soma_contra_OLIMPO}")


# ==========================================
# BLOCO PRINCIPAL
# ==========================================
print("--- Teste da Função ---")
# Basta chamar a função vazia, ela faz todo o trabalho!
exibeJogosGemini()