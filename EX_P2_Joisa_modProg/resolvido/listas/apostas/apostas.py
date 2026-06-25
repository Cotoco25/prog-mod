# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:33:36 2026

@author: guilh
"""
import random

def apostas():
    lista_megasena = []
    while len(lista_megasena)<6:
        num = random.randint(1,60)
        if num not in lista_megasena:
            lista_megasena.append(num)
    print(f'LISTA MEGASENA: {lista_megasena}')
    arq = open('apostas16junho.txt', 'r')
    for linha in arq:
        linha = linha.rstrip()
        linha = linha.split(',')
        nome = linha[0]
        num = int(linha[1])
        print(f'Jogador: {nome}')
        for i in range(num):
            contador = 0
            linha_nova = arq.readline()
            linha_nova = linha_nova.rstrip()
            linha_nova = linha_nova.split(',')
            lista_bet = [linha_nova[0], linha_nova[1], linha_nova[2], linha_nova[3], linha_nova[4], linha_nova[5]]
            for item in lista_bet:
                if int(item) in lista_megasena:
                    contador += 1
            print(f'Aposta: {lista_bet} -> {contador}')
    arq.close()

def teste():
    arq = open('apostas16junho.txt', 'r')
    for linha in arq:
        linha = linha.rstrip()
        linha = linha.split(',') #o split faz a linha virar uma lista, dividida pelo oq vc botou
        print(linha)
    arq.close()

apostas()
print()
print()
# teste()