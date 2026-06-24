# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 15:42:27 2026

@author: guilh
"""

lHeroi= ['batman','superman','wolverine','vampira','tempestade',
'xavier','hulk','flash','spyderman','venom']

lVotos=[ 2990, 2100, 3350, 1122, 1213, 2451, 2855, 1002, 2705, 1567]

def cria_lista_ordenada_dec(lista1,lista2):
    listaFinal = []
    while (len(lista1))>0:
        voto_max = max(lista2)
        pos = lista2.index(voto_max)
        nom = lista1[pos]
        listaFinal.append([nom,voto_max])
        lista1.pop(pos)
        lista2.pop(pos)
    print(lista1)
    print()
    print(lista2)
    print()
    return listaFinal

print(cria_lista_ordenada_dec(lHeroi,lVotos))