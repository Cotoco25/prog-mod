# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:23:44 2026

@author: G2610837
"""

def conversaolibras(nlibras):
    return nlibras*1.23


def conversaodolar(ndolar):
    return ndolar*5.24


nlibras = float(input("Quantas libras você quer converter para dolar? "))
libra_dolar = conversaolibras(nlibras)


ndolar = float(input("Quantos dolares você quer converter para libras? "))
dolar_real = conversaodolar(ndolar)




print(f"{nlibras:.1f}libras - {libra_dolar:.1f}USD$")
print(f"{ndolar:.1f}USD$ - {dolar_real:.1f}BRL$")
print(f"{nlibras:.1f}libras - {dolar_real:.1f}USD$ - {libra_dolar_real:.1f}BRL$")