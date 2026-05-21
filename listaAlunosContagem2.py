# -*- coding: utf-8 -*-
"""
Created on Thu May 21 12:15:30 2026

@author: PC51
"""

# A) Escreva uma função, denominada criaListaAlunoEMedia,
# que receba uma lista de alunos, que é uma lista de sublistas, 
# em que cada sublista tem as seguintes informações de um aluno:
# nome, curso, nota1 e nota2,
# e construa e retorne uma nova lista em que cada elemento é 
# uma lista com nome e media do aluno

def criaListaAlunoEMedia(lista):
    listaNova = []
    for al in lista:
        md = round( (al[2]+al[3])/2 ,1)
        listaNova.append( [ al[0],md ] )
    return listaNova


# B) Sabendo que os cursos são: PROD,COMP,ELET,MAT,AMB,FIS e ECO escreva uma 
# função que receba uma lista de alunos como a descrita no item A 
# e construa e retorne uma nova lista em que cada elemento é 
# uma (sub)lista com CURSO e quantidade de alunos que fazem esse curso.

def soma(lista,curso):
    soma = 0
    for al in lista:
        if al[1] == curso:
            soma += 1
    return soma

def receba(lista):
    #listaCurso: ["PROD","COMP","ELET","MAT","AMB","FIS", "ECO"]
    for al in lista:
        somaProd = soma(lista,"PROD")
        somaComp = soma(lista,"COMP")
        somaElet = soma(lista,"ELET")
        somaMat = soma(lista,"MAT")
        somaAmb =soma(lista,"AMB")
        somaFis = soma(lista,"FIS")
        somaEco = soma(lista,"ECO")
    return print(f"PROD: {somaProd}")

            


#BP
lalunos= [ ['lala','PROD',7.6,9.4],  ['dede','PROD',4.6,3.8],
          ['lele','COMP',2.6,5.5],  ['kaka','ELET',5.4,6.2],
          ['dudu','COMP',6.2,8.3],  ['vivi','AMB',7.1,5.6],
          ['lili','MAT',9.3,8.4],  ['guda','ELET',7.2,8.9],
          ['vava','FIS',9.1,7.4],  ['zaza','ELET',7.4,5.6],
          ['gigi','ECO',3.3,2.4],  ['lolo','FIS',7.4,8.1],
          ['tete','MAT',7.5,3.8],  ['buba','AMB',8.6,9.4]
          ]

print(criaListaAlunoEMedia(lalunos))
receba(lalunos)