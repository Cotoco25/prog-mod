# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 12:10:18 2026

@author: PC37
"""

def calculaBonus(vendas):
    bonus1 = vendas//10000
    x = vendas-bonus1*10000
    bonus2 = x//1000
    bonus_total = (bonus1*1000 + 90*bonus2)
    return bonus_total

def totalDeBonusDaEmpresa(n):
    soma=0
    m = n
    while m>0:
        print("Empregado",1+n-m)
        v1 = int(input("Qual o bonus desse as vendas desse funcionario: "))
        calculaBonus(v1)
        soma += calculaBonus(v1)
        m = m - 1
    return print("Valor total de bonus:",soma)



print(calculaBonus(83400))
print(calculaBonus(2080))

totalDeBonusDaEmpresa(5)