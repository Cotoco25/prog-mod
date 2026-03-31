# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:42:18 2026

@author: PC64
"""


temperatura = float(input("Entre a temperatura: "))

print("------------------------------------")
print(temperatura)

if temperatura > 39:
    print("Muito Calor")
else:
    if temperatura >28:
        print("Calor")
    else:
        if temperatura >20:
            print("Adequado")
        else:
            if temperatura>13:
                print("Fresco")
            else:
                if temperatura <=13:
                    print("Frio")


print("-----------------------------------")