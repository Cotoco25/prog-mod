# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#FUNÇAO: calcarearet
#RECEBE: base e altura
#RETORNA: a area calculada
#https://pythontutor.com/visualize.html#mode=display


def calcarearet (base, altura):
    area = base*altura
    return area

def moldura(tam,carac):
    print(tam*carac)



a = float(input("Qual o tamanho de A? "))
b = float(input("Qual o tamanho de B? "))
c = float(input("Qual o tamanho de C? "))
d = float(input("Qual o tamanho de D? "))

area_maior = calcarearet(a,b)
area_menor = calcarearet(c,d)
areapint = area_maior - area_menor
print()
moldura(30,"=")
print(f"A area pintada é: {areapint:.1f}") #:.1f escolhe quantas casas decimais vai ter
moldura(30,"=")