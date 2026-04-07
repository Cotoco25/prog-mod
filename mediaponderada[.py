# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 11:45:15 2026

@author: PC32
"""

#Guilherme Ressiguier Ribeiro Tostes
#2610837
#33C
#Declaração de autoria: declaro que este documento foi produzido em sua totalidade por mim
#-----------------------------------------------------------------------------
#a)

def calcula_media_ponderada(x1,x2,x3,p1,p2,p3):
    return ((x1*p1)+(x2*p2)+(x3*p3))/(p1+p2+p3)

x1 = float(input("Digite a nota da prova 1: "))
x2 = float(input("Digite a nota da prova 2: "))
x3 = float(input("Digite a nota da prova 3: "))
p1 = float(input("Digite o peso da prova 1: "))
p2 = float(input("Digite o peso da prova 2: "))
p3 = float(input("Digite o peso da prova 3: "))

print("A media ponderada é: ",calcula_media_ponderada(x1,x2,x3,p1,p2,p3))
print()
print()
print()
#-----------------------------------------------------------------------------
#b)

y1 = float(input("Digite a nota da prova 1 do grau 1: "))
y2 = float(input("Digite a nota da prova 2 do grau 1: "))
y3 = float(input("Digite a nota da prova 3 do grau 1: "))
print()
z1 = float(input("Digite a nota da prova 1 do grau 2: "))
z2 = float(input("Digite a nota da prova 2 do grau 2: "))
z3 = float(input("Digite a nota da prova 3 do grau 2: "))
print()

grau_1 = calcula_media_ponderada(y1,y2,y3,2,1,1)
print("Nota do grau 1: ",grau_1)
print()
grau_2 = calcula_media_ponderada(z1,z2,z3,5,2,3)
print("Nota do grau 2: ",grau_2)
print()

grau_t = float(input("Digite a nota do trabalho: "))
print()

def calculo_nota_final(grau_1,grau_2,grau_t):
    return ((grau_1)+(grau_2*2)+(grau_t*2))/5

print("Nota final do aluno: ", calculo_nota_final(grau_1,grau_2,grau_t))
print()

if calculo_nota_final(grau_1,grau_2,grau_t)>=5:
    print("ALUNO APROVADO")
else:
    if calculo_nota_final(grau_1,grau_2,grau_t)>=3:
        print("ALUNO NECESSITA FAZER PROVA FINAL")
    else:
        print("ALUNO REPROVADO")

