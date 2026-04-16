# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:34:34 2026

@author: PC37
"""

import random

def ehPerfeito(n):
    soma=0
    possivel_divisor = 1
    while possivel_divisor <= n//2:
        if n % possivel_divisor == 0:
            soma += possivel_divisor
        possivel_divisor += 1
    return soma == n

ini = random.randint(1,30)
fim = random.randint(1000,10000)
n = ini
while n <= fim:
    if ehPerfeito(n):
        print(n)
    n+=1

print()
print(ini)
print(fim)