# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:03:03 2026

@author: PC64
"""

def pagameia(idade):
    resp = idade<18 or idade>=65
    return resp

#BP
idadelida = int(input("Entre sua idade: "))
print("Paga meia?")
resposta = pagameia(idadelida)
print(resposta)