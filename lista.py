# -*- coding: utf-8 -*-
"""
Created on Tue May 12 12:40:25 2026

@author: PC42
"""

la = [11, 54, 33] #lista 3 elementos

lb = [12, "alo", 2.5]

lc = []

ld = [23, [12,54,"au",3], 10, 99, 88, "ui"] #6 elementos

print(la[1]) #54

def ExibeLista1(ls):
    print('\nElementos da lista (com posições):')
    tam = len(ls)
    ind = 0
    while ind < tam:
        print(f"Elem: ls{ind} - Pos:{ind}")
        ind +=1

def ExibeLista2(ls):
    print("\nElementos da lista:")
    for elemento in ls:
        print(elemento)

def ExibeLista3(ls):
    print("\nPosição e Elementos da lista:")
    for pos,elem in enumerate(ls):
        print(f'Posição:{pos} - Elemento: {elem}')
        

papapa = ExibeLista1(la)
print(papapa)

bababa = ExibeLista2(la)
print(bababa)

lalala = ExibeLista3(la)
print(lalala)