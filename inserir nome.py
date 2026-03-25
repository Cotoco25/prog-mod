# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:22:29 2026

@author: G2610837
"""

#print("dados", nome, idade, alt)

#msg = "aluno %s tem %d anos e %f de altura" %(nome, idade, alt)
#print(msg)


#input SEMPRE retorna string (str)
nome = input('Qual o seu nome? ') #oq o usuario colocar vira o nome dele
idade = int (input('Qual a sua idade? '))
alt = float(input('Qual a sua altura? '))


#/t faz um espaço grande na mensagem
print(f'{nome} tem {idade} anos e terá {idade+1} em 2027')
print(f'e você tem {alt:.2f} de altura, anão')

