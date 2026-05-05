# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:44:41 2026

@author: PC-PROF
"""

# AQUI: precisa da POSICAO
# Escreva uma função denominada achaPosicao,
# que receba uma string e um caractere e 
# retorne a posição da primeira ocorrencia 
# do caractere na string. Caso o caractere não 
# esteja na string, retorne -1
# exemplo: BANANA   e  N   retorna 2 (posicao)

def achaPosicao(s, caracDesejado):
    tam = len(s)
    ind = 0
    while ind<tam:
        if s[ind]== caracDesejado:
            return ind  #achou!! retorna a posicao 
        ind+=1 
    # testou todos e não achou
    return -1 

#AQUI : enumerate
def achaPosicaoVS2(s, caracDesejado):
    for pos,elem in enumerate(s):
        if elem == caracDesejado:
            return pos 
    return -1


# AQUI: não precisa da posicao
# Escreva uma função denominada contaCaractere,
# que receba uma string e um caractere e 
# retorne a quantidade de ocorrencias do caractere 
# na string
# ex: BANANA  e  A  retorna 3 (qtd)

def contaCaractere(s,caracDesejado):
    qtdOc=0 
    for carac in s:
        if carac == caracDesejado:
            qtdOc+=1 
    return qtdOc

#BP
palavra='BANANAS'
letra='N'
pos = achaPosicaoVS2(palavra,letra)
if pos != -1:
    print(f'{letra} está na posicao {pos} em {palavra}')
else:
    print(f'{letra} não está em {palavra}')

palavra='BANANAS'
letra='A'
pos = achaPosicao(palavra,letra)
if pos != -1:
    print(f'{letra} está na posicao {pos} em {palavra}')
else:
    print(f'{letra} não está em {palavra}')

palavra='BOLINHO'
letra='A'
pos = achaPosicao(palavra,letra)
if pos != -1:
    print(f'{letra} está na posicao {pos} em {palavra}')
else:
    print(f'{letra} não está em {palavra}')