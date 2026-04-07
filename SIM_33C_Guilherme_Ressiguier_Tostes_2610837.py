# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:12:58 2026

@author: PC32
"""

#Guilherme Ressiguier Ribeiro Tostes
#2610837
#33C
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim

#a)

def calcular_valor_final(c,i,n):
    return c*(1+i/100)**n

c = float(input("Digite a capital inicial: "))
i = float(input("Digite a taxa mensal em %: "))
n = float(input("Digite o numero de meses do investimento: "))

print("O valor final do investimento é: ", calcular_valor_final(c,i,n))
print()

#------------------------------------------------------------------------------
#b)
#c)
  
c1 = float(input("Digite a capital inicial do investimento 1: "))
i1 = float(input("Digite a taxa mensal em % do investimento 1: "))
n1 = float(input("Digite o numero de meses do investimento: "))
c2 = float(input("Digite a capital inicial do investimento 2: "))
i2 = float(input("Digite a taxa mensal em % do investimento 2: "))
n2 = float(input("Digite o numero de meses do investimento 2: "))
print()

def avalia_dois_investimentos(c1, i1, n1, c2,i2,n2):
    print("===DADOS DO INVESTIMENTO 1===")
    print("Capital inicial do investimento 1: ",c1)
    print("Taxa mensal to investimento 1: ",i1)
    print("Numero de meses do investimento 1: ",n1)
    print()
    print("===DADOS DO INVESTIMENTO 2===")
    print("Capital inicial do investimento 2: ",c2)
    print("Taxa mensal to investimento 2: ",i2)
    print("Numero de meses do investimento 2: ",n2)

avalia_dois_investimentos(c1, i1, n1, c2,i2,n2)
#-------------------------------------------------------------------------------
#c)
def calcular_valor_final1(c1,i1,n1):
    return c1*(1+i1/100)**n1

def calcular_valor_final2(c2,i2,n2):
    return c2*(1+i2/100)**n2

if calcular_valor_final1(c1,i1,n1) > calcular_valor_final2(c2,i2,n2):
    print ("COMPARAÇÃO")
    print("==================")
    print("O Primeiro investimento teve MAIS lucro ")
    print ("Diferença: ",calcular_valor_final1(c1,i1,n1)-calcular_valor_final2(c2,i2,n2))
else:
        print ("COMPARAÇÃO")
        print("==================")
        print("O Segundo investimento teve MAIS lucro ")
        print("Diferença: ",calcular_valor_final2(c2,i2,n2)-calcular_valor_final1(c1,i1,n1))

    