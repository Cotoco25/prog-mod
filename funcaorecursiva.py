# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""



def fatorial(n):
    if n == 0:
        return 1
    aux = fatorial(n-1)
    resp = n*aux
    return resp

print(fatorial(4))

def potencia(base,expoente):
    if expoente == 0:
        return 1
    aux = potencia(base,expoente-1)
    resp = base*aux
    return resp

print(potencia(3,4))

def exibeMsgRec(msg,x):
    if x == 0:
        print('---fim---')
        return
    print(msg)
    exibeMsgRec(msg,x-1)
    print('thau')


def conta(x):
    #caso base
    if x < 10:
        return 1
    
    #caso geral
    #n = x%10 nao precisa: a contribuicao da unidade e sempre 1
    n = x//10
    resp = 1 + conta(n)
    return resp

print(conta(2020207202020720202072020207202020720202072020207202020720202072020))

print(8%2)

def contaPares(x):
    if x < 10:
        if x%2 == 0:
            return 1
        else:
            return 0
    
    #caso geral
    unidade = x%10
    numAntecede = x//10
    if unidade%2 == 0:
        return 1 + contaPares(numAntecede)
    else:
        return contaPares(numAntecede)