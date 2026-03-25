# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:23:47 2026

@author: G2610837
"""

#   NOME: Guilherme R R Tostes
#   MAT: 2610837
#   33C
#   Prof: Josia
#   Exercicio: IMC

nome = input('Qual é o seu nome? ')
peso = float(input('Qual o seu peso? '))
alt = float(input('Qual a sua altura? '))


IMC_resolvido = (peso / alt**2)

print(f'{nome} IMC igual a {IMC_resolvido}.')

