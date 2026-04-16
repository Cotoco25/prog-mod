# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

cont = 0
qtd = int(input("Quantas pessoas: "))

while cont < qtd:
    print(15*"-")
    nome = input("Nome: ")
    plano = input("Plano: ")
    qtd = qtd-1
    if plano == ("diamante"):
        desconto = 50
    else:
        idade = int(input("Idade: "))
        if idade < 12:
            desconto = 40
        elif idade >= 60:
            desconto = 30
        elif plano == ("ouro"):
            desconto = 20
        elif plano == ("prata"):
            desconto = 10
        else:
            desconto = 0
