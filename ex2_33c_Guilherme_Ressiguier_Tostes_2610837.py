# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:04:51 2026

@author: G2610837
"""
#   NOME: Guilherme R R Tostes
#   MAT: 2610837
#   33C
#   Prof: Josia
#   Exercicio: ano futuro

import random


ano_corrente = int (input('Qual é o ano corrente? '))
ano_futuro = random.randint(ano_corrente, 2050)

nome = input('Qual o seu nome? ')
idade = int (input('Qual é sua idade? '))
idade_futura = (idade + ano_futuro - ano_corrente)


print(f'Em {ano_futuro}, {nome} terá {idade_futura}.')
