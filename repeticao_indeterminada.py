# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:34:40 2026

@author: PC41
"""

idade= int(input("Qual a sua idade? "))
soma=0

while idade>-1:
    idade = int(input("Qual a sua idade? "))
    if idade>50:
        soma+=1


print(f"n de pessoas +50: {soma}")