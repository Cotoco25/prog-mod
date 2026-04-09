# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
import time

print("ola"+"a")

nomelido = input("Qual o seu nome: ")
x = int(input("Quantas vezes? "))

print("-"*30)
cont = 0
while cont <x:
    print("oi", nomelido)
    cont+=1         #cont = cont+1
print("-"*30)
print()

comeco = int(input("Inicio: "))
final = int(input("final: "))

numero = comeco
while numero<=final:
    print(numero)
    time.sleep(1)
    numero+=1

print()

print("Antes da repeticao começar --")
cont2 = 0
while cont2 <100:
    print("ola"+"a"*cont2)
    time.sleep(1)
    cont2+=1         #cont = cont+1
print("Apos o termino da repetição")