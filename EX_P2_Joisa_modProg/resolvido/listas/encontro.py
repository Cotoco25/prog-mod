# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 11:38:28 2026

@author: PC41
"""


lparc= [['lala', ['restaurante','bar','praia']], ['nena', ['cinema','leitura','praia']],
 ['vivi', ['cinema','leitura','teatro']], ['lele', ['restaurante','bar','praia']],
 ['nina', ['cinema','leitura','praia']], ['tita', ['cinema','leitura','teatro']],
 ['leda', ['viagem','danca','esporte']], ['gege', ['praia','leitura','viagem']],
 ['tati', ['cinema','leitura','dormir']], ['babi', ['viagem','cachorro','praia']],
 ['tata', ['cachorro','leitura','praia']], ['zaza', ['cinema','gato','cachorro']]
 ] 

listinha = ['praia','leitura','tv']

def para_um_encontro(lista,lista2):
    listaFinal = []
    for item in lista:
        if (lista2[0] in item[1] and lista2[1] in item[1]) or (lista2[0] in item[1] and lista2[2] in item[1]) or (lista2[1] in item[1] and lista2[2] in item[1]) or (lista2[0] in item[1] and lista2[1] in item[1] and lista2[2] in item[1]):
            listaFinal.append(item[0])
    return listaFinal

print(para_um_encontro(lparc, listinha))