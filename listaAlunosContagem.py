# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:23:36 2026

@author: PC51
"""

# A) Escreva uma função, denominada exibeAlunos,
# que receba uma lista de sublistas, em que cada sublista 
# tem as seguintes informações de um aluno:nome, curso, nota1 e nota2,
# e exiba nome,curso e media dos alunos.

def exibeAlunos(lista):
    print("\nAlunos da lista:")
    for al in lista:
        media=(al[2] + al[3])/2
        print(f"Nome: {al[0]} - Curso: {al[1]} - Media: {media:.1f}")

# B) Escreva uma função, denominada buscaAluno,
# que receba uma lista de sublistas, em que cada sublista 
# tem as seguintes informações de um aluno:nome, curso, nota1 e nota2,
# e o nome de uma aluno, e retorne a posição desse aluno 
# na lista. Caso o aluno não esteja na lista
# a função retorna -1 (poderia também ser pedido para retornar None)

def buscaAluno(lista,nome):
    print(f"Posição do aluno: {nome}")
    for ind, al in enumerate(lista):
        if nome == al[0]:
            return ind
    return -1
    

# C) Escreva uma função, denominada exibeAlunosDeUmCurso,
# que receba uma lista de sublistas, em que cada sublista 
# tem as seguintes informações de um aluno:nome, curso, nota1 e nota2,
# e um curso e exiba nome e as notas dos alunos desse curso.

def exibeAlunosDeUmCurso(lista,curso):
    print(f"QTD de alunos no curso: {curso}")
    for al in lista:
        if al[1] == curso:
            print(f'Nome: {al[0]} - Nota1: {al[2]} - Nota2: {al[3]}')

# D) Escreva uma funcao, denominada criaListaNomesDeUmCurso,
# que receba uma lista de alunos e um curso, e construa (CRIA) 
# e retorne (RETORNAR) uma nova lista somente com os nomes dos alunos 
# desse curso.

def criaListaNomesDeUmCurso(lista,curso):
    listaNova = []
    for al in lista:
        if al[1] == curso:
            listaNova.append(al[0])
    return listaNova




#BP
lalunos= [ ['lala','PROD',7.6,9.4],  ['dede','PROD',4.6,3.8],
          ['lele','COMP',2.6,5.5],  ['kaka','ELET',5.4,6.2],
          ['dudu','COMP',6.2,8.3],  ['vivi','AMB',7.1,5.6],
          ['lili','MAT',9.3,8.4],  ['guda','ELET',7.2,8.9],
          ['vava','FIS',9.1,7.4],  ['zaza','ELET',7.4,5.6],
          ['gigi','ECO',3.3,2.4],  ['lolo','FIS',7.4,8.1],
          ['tete','MAT',7.5,3.8],  ['buba','AMB',8.6,9.4]
          ]


exibeAlunos(lalunos)
print()
print(buscaAluno(lalunos,"gigi"))
print()
exibeAlunosDeUmCurso(lalunos,"FIS")
print()
print(criaListaNomesDeUmCurso(lalunos,"FIS"))