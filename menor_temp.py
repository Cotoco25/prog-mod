# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:45:21 2026

@author: PC41
"""
import math
import random

menortemp = math.inf
soma = 0
media = 0
n=6
dias = 4
day = 1

while 0<dias:
    while 0 < n:
        temp = random.randint(-250,360)/10
        if temp < menortemp:
            menortemp = temp
        n -= 1
    n +=6
    print(f"A menor temperatura do dia {day} foi {menortemp}C")
    soma += menortemp
    menortemp = math.inf
    dias -=1
    day +=1

media = soma/4
print(f"A media das menor temp foi {media:.1f}C")




