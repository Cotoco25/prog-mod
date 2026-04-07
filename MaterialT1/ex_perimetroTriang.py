# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 12:48:37 2022

@author: PC-PROF
"""

def calculaLado(x1,y1,x2,y2):
    lado=((x2-x1)**2+ (y2-y1)**2)**0.5
    return lado

def calculaPerimetro(ax,ay,bx,by,cx,cy):
    lado1 = calculaLado(ax,ay,bx,by)
    lado2 = calculaLado(bx,by,cx,cy)
    lado3 = calculaLado(ax,ay,cx,cy)
    per= lado1+lado2+lado3
    return per


#Parte Principal
xa= float(input('Entre x do vértice A:'))
ya= float(input('Entre y do vértice A:'))
xb= float(input('Entre x do vértice B:'))
yb= float(input('Entre y do vértice B:'))
xc= float(input('Entre x do vértice C:'))
yc= float(input('Entre y do vértice C:'))

perimetro= calculaPerimetro(xa,ya,xb,yb,xc,yc)
print(perimetro)

