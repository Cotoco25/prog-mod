# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

#Meu programa

#idade = float(input('entre sua idade: '))

#EhMaiorDeIdade = idade >= 18
#print(EhMaiorDeIdade)

#Progama da prof

def EhMaiorDeIdade(idade):
    resp = idade>=18
    return resp

#BP
IdadeLida = int(input("Entre Idade: "))
print ("Maior de Idade?")
resposta = EhMaiorDeIdade(IdadeLida)
print(resposta)