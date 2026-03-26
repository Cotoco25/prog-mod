# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 12:05:03 2026

@author: PC34
"""

def calcdistentrepontos(x1,y1,x2,y2):
    dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return dist

#BLOCO PRINCIPAL
xa=float(input("Entre coordenada xa"))
ya=float(input("Entre coordenada ya"))
xb=float(input("Entre coordenada xb"))
yb=float(input("Entre coordenada yb"))

dist_ab = calcdistentrepontos(xa,ya,xb,yb)
print (dist_ab)
