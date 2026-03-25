# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:48:25 2026

@author: G2610837
"""

import time

def mediadasprovas (prova, test1, test2):
    media = prova*.7 + test1*.1 + test2*.2
    return media

def moldura(tam,carac):
    print(tam*carac)

print("Faça seu login de estudante:")
nomealuno = input("Qual o nome do aluno? ")
a = float(input("Bloco 1: Nota da prova? "))
b = float(input("Bloco 1: Nota do teste 1? "))
c = float(input("Bloco 1: Nota do teste 2? "))

print()

a2 = float(input("Bloco 2: Nota da prova? "))
b2 = float(input("Bloco 2: Nota do teste 1? "))
c2 = float(input("Bloco 2: Nota do teste 2? "))


mediabloco1 = mediadasprovas(a,b,c)
mediabloco2 = mediadasprovas(a2,b2,c2)
mediatotal = (mediabloco1 + mediabloco2)/2

print()
print("carregando...")
time.sleep(2)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("DADOS OBTIDOS!")
time.sleep(1.5)


print()
print("BOLETIM")
moldura(50,"=")
print("Estudante: ", nomealuno)
print()
print(f"Nota da prova bloco 1: {a:.1f}")
print(f"Nota do primeiro teste do bloco 1: {b:.1f}")
print(f"Nota do segundo teste do bloco 1: {c:.1f}")
moldura(50,"=")
print(f"Nota da prova bloco 2: {a2:.1f}")
print(f"Nota do primeiro teste do bloco 2: {b2:.1f}")
print(f"Nota do segundo teste do bloco 2: {c2:.1f}")
print(f"Media do grau 1: {mediabloco1:.1f}")
print(f"Media do grau 2: {mediabloco2:.1f}")
print(f"A media dos dois graus é: {mediatotal:.1f}") #:.1f escolhe quantas casas decimais vai ter
moldura(50, "=")
if mediatotal>6:
    print(f"Parabens {nomealuno}, você está aprovado com uma media {mediatotal:.1f}!")
else:
    print(f"O estudante {nomealuno} não está com a media dos seus graus acime de 6, sendo respectivamente {mediatotal:.1f}, e tera que repetir de ano.")

moldura(50,"=")