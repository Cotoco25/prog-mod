# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:21:09 2026

@author: PC41
"""



def china():
    arq = open('dadospessoas.txt','r')
    lista = [['rato', 0], ['boi', 0], ['tigre', 0], ['coelho', 0], ['dragao', 0], ['cobra', 0], ['cavalo', 0], ['carneiro', 0], ['macaco', 0], ['galo', 0], ['cao', 0], ['porco', 0]]
    for linha in arq:
        linha.rstrip()
        linha = linha.split(';')
        ano = int(linha[1][-4:])
        if ano%12 == 0:
            lista[0][1] +=  1
        if ano%12 == 1:
            lista[1][1] +=  1
        if ano%12 == 2:
            lista[2][1] +=  1
        if ano%12 == 3:
            lista[3][1] +=  1
        if ano%12 == 4:
            lista[4][1] +=  1
        if ano%12 == 5:
            lista[5][1] +=  1
        if ano%12 == 6:
            lista[6][1] +=  1
        if ano%12 == 7:
            lista[7][1] +=  1
        if ano%12 == 8:
            lista[8][1] +=  1
        if ano%12 == 9:
            lista[9][1] +=  1
        if ano%12 == 10:
            lista[10][1] +=  1
        if ano%12 == 11:
            lista[11][1] +=  1
    arq.close()
    return lista

print(china())