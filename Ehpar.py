# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:56:35 2026

@author: PC64
"""

def Ehpar(numero):
    resp = numero%2 ==0
    return resp

#BP
numerolido = int(input("Entre o seu numero: "))
print ("Numero é par?")
resposta = Ehpar(numerolido)
print(resposta)
