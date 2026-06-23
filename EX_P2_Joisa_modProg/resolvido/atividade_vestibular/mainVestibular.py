# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:02:02 2026

@author: guilh
"""

def criaListaMaioresNotas():
    arq = open('resultadosvestibular2025.txt', 'r')
    listaFinal = []
    for linha in arq:
        linha = linha.rstrip()
        linha = linha.split(';')
        nom = linha[0]
        tam = int(linha[1])
        maiorNota = 0
        alunofinal = []
        for i in range(tam):
            linha = arq.readline()
            linha = linha.split(';')
            nota = float(linha[1])
            if nota>maiorNota:
                maiorNota = nota
                alunofinal = [linha[0]]
            elif nota==maiorNota:
                alunofinal.append(linha[0])
        listaFinal.append([nom,maiorNota,alunofinal])
    arq.close()
    return listaFinal     

def exibeCursos(lista):
    for coisa in lista:
        print(f'==== Curso:{coisa[0]} - Nota Maxima: {coisa[1]} ===')
        listaNova = coisa[2]
        for coisanova in listaNova:
            print(f'---> {coisanova}')
        print()

def escreveArq(nome, lista):
    arq = open(nome, 'w')
    for item in lista:
        arq.write(f'{item[0]}, {item[1]}\n')
        for i in item[2]:
            arq.write(f'{i},')
        arq.write('\n')
    arq.close()


lista = criaListaMaioresNotas()
print(criaListaMaioresNotas())
print()
exibeCursos(lista)
escreveArq('arquivoPronto.txt', lista)
