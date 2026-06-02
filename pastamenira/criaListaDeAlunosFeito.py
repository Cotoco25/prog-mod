# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 11:54:59 2026

@author: PC-PROF
"""

# Em um arquivo texto chamado alunos.txt cada linha 
# tem as seguintes informações de um aluno, separadas por ; 
# nome, curso, nota1 e nota2.

# Escreva uma função que crie e retorne uma lista 
# em que cada elemento é uma lista com nome, curso e duas 
# notas(float) de um aluno, a partir dos dados do arquivo 
# alunos.txt

def criaListaDeAlunos():
    lalunos=[]
    
    arq= open('alunos.txt' , 'r')
    for linha in arq:
        linha = linha.strip()
        #print(linha) 
        lst = linha.split(';')
        lst[2] = float(lst[2])
        lst[3] = float(lst[3])
        #print('-->',lst)
        lalunos.append(lst)
        
    arq.close()
    
    return lalunos
    
#BP
listaAlunos= criaListaDeAlunos()
print('\n==== LISTA DE ALUNOS: ====')
print(listaAlunos)
    
    
    
    