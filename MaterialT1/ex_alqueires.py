# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 22:22:30 2025

@author: joisa
"""

def converteAlqueirePaulistaEmM2(alqPaulista):
    return alqPaulista*24200

def converteAlqueireDoNorteEmM2(alqNorte):
    return alqNorte*27225

def exibeTotalDeTerras(alqPaulista,alqNorte):
    totM2= converteAlqueirePaulistaEmM2(alqPaulista)+\
           converteAlqueireDoNorteEmM2(alqNorte)
    print(f'Total de terras: {totM2:.1f} m²')
    
#Bloco Principal
alqueiresPaulista= float(input('Entre qtd de alqueires paulistas:'))
alqueiresDoNorte= float(input('Entre qtd de alqueires do norte:')) 
exibeTotalDeTerras(alqueiresPaulista,alqueiresDoNorte)