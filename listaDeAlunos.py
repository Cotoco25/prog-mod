# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:03:12 2026

@author: joisa
"""

# A) Escreva uma função, denominada exibeAlunos,
# que receba uma lista de sublistas, em que cada sublista 
# tem as seguintes informações de um aluno:nome, curso, nota1 e nota2,
# e exiba nome,curso e media dos alunos.
def exibeAlunos(lal):
    print('\nAlunos da lista:')
    for al in lal:
        md=(al[2]+al[3])/2
        print(f'Nome:{al[0]} - Curso:{al[1]} - Media:{md:.1f}')
        
# B) Escreva uma função, denominada buscaAluno,
# que receba uma lista de sublistas, em que cada sublista 
# tem as seguintes informações de um aluno:nome, curso, nota1 e nota2,
# e o nome de uma aluno, e retorne a posição desse aluno 
# na lista. Caso o aluno não esteja na lista
# a função retorna -1 (poderia também ser pedido para retornar None)

# C) Escreva uma função, denominada exibeAlunosDeUmCurso,
# que receba uma lista de sublistas, em que cada sublista 
# tem as seguintes informações de um aluno:nome, curso, nota1 e nota2,
# e um curso e exiba nome e as notas dos alunos desse curso.

# D) Escreva uma funcao, denominada criaListaNomesDeUmCurso,
# que receba uma lista de alunos e um curso, e construa (CRIA) 
# e retorne (RETORNAR) uma nova lista somente com os nomes dos alunos 
# desse curso.

#BP
lalunos= [ ['lala','PROD',7.6,9.4],  ['dede','PROD',4.6,3.8],
          ['lele','COMP',2.6,5.5],  ['kaka','ELET',5.4,6.2],
          ['dudu','COMP',6.2,8.3],  ['vivi','AMB',7.1,5.6],
          ['lili','MAT',9.3,8.4],  ['guda','ELET',7.2,8.9],
          ['vava','FIS',9.1,7.4],  ['zaza','ELET',7.4,5.6],
          ['gigi','ECO',3.3,2.4],  ['lolo','FIS',7.4,8.1],
          ['tete','MAT',7.5,3.8],  ['buba','AMB',8.6,9.4]
          ]

print('\n-- Teste da exibeAlunos -- ')
exibeAlunos(lalunos)





