# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:15:07 2026

@author: PC-PROF
"""

# A) Escreva uma função que receba uma lista 
# e retorne a quantidade de elementos do 
# tipo string em qualquer nivel da lista 
# (Considerando todos os niveis da lista)

def contaStringRec(ls):
    cont=0
    for elem in ls:
        if type (elem)== str:
            cont+=1 
        elif type(elem)== list:
            cont+=contaStringRec(elem) # elem é uma listinha
    return cont

# B) Escreva uma função que receba uma lista e um valor X 
#     e retorne a quantidade de valores numericos maiores do que
#     x em qualquer nivel da lista
def contaAcimaLimRec(ls,x):
    cont=0
    for el in ls:
        if type(el)==int or type(el)==float :
            if el>x:
                cont+=1 
        elif type(el)==list:
            qtdNaListinha = contaAcimaLimRec(el,x)
            cont+=qtdNaListinha
    return cont

# C) Escreva uma função que receba uma lista e substitua 
#    toda string  pelo seu tamanho em qualquer nivel da lista
def substituiStringsRec(ls):
    for ind,el in enumerate(ls):
        if type(el)==str:
            ls[ind]=len(el)
        elif type(el)==list:
            substituiStringsRec(el)

# D) Escreva uma função que receba uma lista 
#     e retorne a soma dos  valores numericos 
#     da lista, em qualquer nivel da lista
def somaRec(ls):
    total=0
    for el in ls:
        if type(el)==int or type(el)==float:
            total+=el 
        elif type(el)==list:
            total+=somaRec(el)
    return total
  
# E) Escreva uma função recursiva que receba uma 
# lista e um caractere e retorne a quantidade 
# de strings com esse caractere, em qualquer 
# nivel da lista
def contaTemCaractere(ls,carac):
    cont=0 
    for el in ls:
        if type(el)==str:
            if carac in el:
                cont+=1     #contribuicao da string:  1 (ou não contribui)
        elif type(el)==list:
            cont+=contaTemCaractere(el,carac)
    return cont

# F) Escreva uma função recursiva que receba uma 
# lista e um caractere e retorne a quantidade 
# de ocorrencias desse caractere na lista, em qualquer 
# nivel da lista
def contaOcorrenciasCaractere(ls,carac):
    cont=0 
    for el in ls:
        if type(el)==str:
             cont+=el.count(carac) #contribuicao da string depende da string
        elif type(el)==list:
            cont+=contaOcorrenciasCaractere(el,carac)
    return cont

# G) Escreva uma função recursiva que receba uma 
# lista e um valor x e retorne True, se existe 
# ao menos um valor numerico maior do que x na 
# lista (em qq nivel) ou False, caso contrario
def temMaiorQue(ls,x):
    for el in ls:
        if type(el)==int or type(el)==float:
            if el>x:
                return True 
        elif type(el)==list:
            if temMaiorQue(el,x)==True:  # if temMaiorQue(el,x):
                return True 
    return False

# H) Escreva uma função recursiva que receba uma 
# lista e um valor x e retorne True, se NÃO existe 
# nenhum valor numerico maior do que x na 
# lista (em qq nivel) ou False, caso contrario


def naoTemMaiorQue(ls,x):
    for el in ls:
        if type(el)==int or type(el)==float:
            if el>x:
                return False
        elif type(el)== list:
            if naoTemMaiorQue(el,x)==False:
                return False
    return True
   

# I) Escreva uma função recursiva, denominada achaMaiorRec, que 
# receba uma lista e retorne o maior valor numerico, em qq 
# nivel da lista. Caso não exista nenhum valor numerico 
# a funcao deve retornar None
# DICA: inicialize a variável maior com None

def achaMaiorRec(ls):
    maior = None
    for el in ls:
        if type(el)== int or type(el)==float:
            if maior==None:
                maior = el
            else:
                if el>maior:
                    maior=el 
        elif type(el)==list:
            maiorDaListinha= achaMaiorRec(el)
            if maior==None:
                maior=maiorDaListinha
            elif maiorDaListinha!=None:
                if maiorDaListinha>maior:
                    maior=maiorDaListinha
    return maior
     
#BP
lz=[12,'au',[44,'uau',14,'ceu'],29.7,'eu',[[13,'mar'],'ze',['sol']],14]
ly=['au',['ui','teu'],'zi']
lx= ['au',['ui',9],'zi']
ld= ['au',['ui','teu'],13]

# print('\nLISTA:',lz)
# qt=contaStringRec(lz)
# print(f'Há {qt} strings na lista')

# print('\nLISTA:',lz)
# qt=contaAcimaLimRec(lz,27)
# print(f'Há {qt} acima de 13 na lista')
# qt=contaAcimaLimRec(lz,20)
# print(f'Há {qt} acima de 13 na lista')  

# print('\nANTES:',lz)
# substituiStringsRec(lz)
# print('\nDEPOIS:',lz)

print(achaMaiorRec(lz))
print(achaMaiorRec(ly))
print(achaMaiorRec(lx))
print(achaMaiorRec(ld))