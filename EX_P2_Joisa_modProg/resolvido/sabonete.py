# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:35:28 2026

@author: guilh
"""

lfarmacias= [['FARMMAH', [ ['BomCheiro',9.20,150], ['Limpex',8.50,18],  ['Glicerinix',5.92,30], ['NutriMilk',6.90,80] ] ],
             ['KIKKAS',  [ ['CleanRose',6.75,40],  ['BomCheiro',7.25,200], ['RosaBranca',9.0, 50] ] ],
             ['CANOINHA',[ ['NutriMilk',5.83,20] , ['CleanRose',8.15,120] ] ] ,
             ['DROGGHY', [ ['CleanRose',4.1,35],  ['BomCheiro',7.75, 60], ['RosaBranca',8.35, 40] ] ],
             ['PHAPHAH', [ ['CleanRose',6.1,85],  ['Glicerinix',5.80, 40],['BomCheiro',6.75, 60] ] ],
             ['FINAFARM',[ ['Limpex',7.87,20]  ] ] ]

def exibe(lista):
    for item in lista:
        nom = item[0]
        listaNova = item[1]
        print(f'===FARMACIA:{nom}====')
        for dado in listaNova:
            print(f'{dado[0]} => {dado[1]} reais - {dado[2]} unidades')
        print()

def boasCompra(lista, x):
    listaSabo = []
    listaNova= []
    for item in lista:
        for i in range(len(item[1])):
            itemSabo = item[1][i][0]
            if itemSabo not in listaSabo:
                listaSabo.append(itemSabo)
    for item in lista:
        listaSaboFinal = []
        nom = item[0]
        for sabo in listaSabo:
            for dado in item[1]:
                if sabo in dado and dado[1]<x:
                    listaSaboFinal.append(sabo)
        listaNova.append([nom,listaSaboFinal])
    return listaNova

def totaisDasMarcas(lista):
    listaFinal = []
    qtd = 0
    for item, pos in lista:
        for sabo in item[1]:
            nomSabo = item[0]
            qtd += item[2]
        

#BP
#exibe(lfarmacias)
print(boasCompra(lfarmacias,100))