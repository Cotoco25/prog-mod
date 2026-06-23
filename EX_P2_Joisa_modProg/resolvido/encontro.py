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

def para_um_encontro(lista):
    listaFinal = []
    for item in lista:
        if (item[1][0] and item[1][1]) or (item[1][0] and item[1][2]) or (item[1][1] and item[1][2]) or (item[1][2] and item[1][1] and item[1][0]) in lista:
            listaNome = []
            listaNome.append(item[0])
            listaFinal.append(listaNome)
    return listaFinal

print(para_um_encontro(lparc))