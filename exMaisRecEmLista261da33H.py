# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:16:45 2026

@author: joisa
"""

# A) Escreva uma função recursiva, denominada contaNoIntervaloRec, 
# que receba uma lista e o inicio e o fim de um intervalo, 
# e retorne a quantidade de valores numéricos no intervalo
# (extremos incluidos), em qualquer nivel da lista
# Assuma inicio <= fim
def contaNoIntervaloRec(ls,ini,fim):
    cont=0
    for el in ls:
        if type(el)==int or type(el)==float: 
            if el>=ini and el <=fim:  #ini<=el<=fim
                cont+=1 
        elif type(el)==list:
            cont+= contaNoIntervaloRec(el,ini,fim)
    return cont
    
# B) Escreva uma função recursiva, denominada temNoIntervaloRec, 
# que receba uma lista e o inicio e o fim de um intervalo, 
# e retorne True, se houver um valor numerico no intervalo 
# em qualquer nivel da lista, ou False, caso contrario
def temNoIntervaloRec(ls,ini,fim):
    for el in ls:
        if type(el)==int or type(el)==float: 
            if el>=ini and el <=fim: 
                return True 
        elif type(el)==list:
            if temNoIntervaloRec(el,ini,fim)==True:
                return True 
    return False        
                
# C) Escreva uma função recursiva, denominada substituiNoIntervaloRec, 
# que receba uma lista e o inicio e o fim de um intervalo, 
# e substitua todo  valor numerico no intervalo pelo inteiro 
# correspondente ao meio do intervalo ,
# em qualquer nivel da lista
def substituiNoIntervaloRec(ls,ini,fim):
    for ind,el in enumerate(ls):
        if type(el)==int or type(el)==float: 
            if el>=ini and el <=fim: 
                ls[ind] = (ini+fim)//2
        elif type(el)==list:
            substituiNoIntervaloRec(el,ini,fim)

            
# D) Escreva uma função, denominada criaCopiaRec, que receba uma lista 
# e um caractere c, e crie e RETORNE um nova lista, em que todas as 
# ocorrencias do caractere recebido devem ser alteradas para *,
# em qualquer nível da lista
def criaCopiaRec(ls,carac):
    novaLista=[]
    for el in ls:
        if type(el) == str:
            novaLista.append(el.replace(carac,'*'))
        elif type(el) == list:
            novaLista.append( criaCopiaRec(el,carac) )
        else:
            novaLista.append(el)
    return novaLista        
            
# E) Escreva uma função, denominada tamanhoMaiorString, que receba uma lista 
# e  retorne o tamanho da maior string, em qualquer nível da lista
# Caso não exista string na lista a função retorna None
# DICA: inicialize Maior com None
def tamanhoMaiorString(ls):
    maior = None
    for el in ls:
        if type(el)==str:
            tamanho= len(el)
            if maior==None or tamanho>maior:
                maior=tamanho 
        elif type(el)==list:
            tamMaiorDaListinha= tamanhoMaiorString(el)
            if maior==None or tamMaiorDaListinha>maior:
                maior=tamMaiorDaListinha
    return maior

# PARA CASA: 
# F) Escreva uma função, denominada criaCopiaDobroRec, que receba uma lista 
# e crie e RETORNE um nova lista, em que todos os valores inteiros da original 
# devem ter seu valor dobrado, em qualquer nível da lista

# G) Escreva uma função recursiva, denominada naoTemStMaiorQue, 
# que receba uma lista e um valor x , e retorne True, se não houver 
# nenhuma string com tamanho  maior do que x, em qualquer nivel da lista, 
# ou False, caso contrario


#BP
lst=[ 12,'sal',35,'olho',[5.6,[13,'roupa','mel',44,63],False,[99,'sol',2,'eu']],True,[114,'morros','ar']]

print(30*'=')
print('\n--A) Teste da contaNoIntervaloRec --')
print('\nLISTA:')
print(lst)
print('\nQuantidade de valores entre 30 e 100')
print(contaNoIntervaloRec(lst,30,100))

print(30*'=')
print('\n--B) Teste da temNoIntervaloRec  --')
print('\nLISTA:')
print(lst)
if temNoIntervaloRec(lst,30,100):
    print('\nHá valores entre 30 e 100 na lista')
else:
    print('Não há valores entre 30 e 100 na lista')
    
if temNoIntervaloRec(lst,45,60):
    print('\nHá valores entre 45 e 60 na lista')
else:
    print('Não há valores entre 45 e 60 na lista')    
    
print(30*'=')
print('\n--C) Teste da substituiNoIntervaloRec com a lista com 30 e 100 --')
print('\nANTES')
print(lst)
substituiNoIntervaloRec(lst,30,100)
print('\nDEPOIS')
print(lst)

print(30*'=')
print('\n--D) Teste da criaCopiaRec com a lista e o caractere o --')
print('\nLISTA:')
print(lst)
print('\nNova Lista:')
nova= criaCopiaRec(lst,'o')
print(nova)
print('\nLISTA:')
print(lst)

print(30*'=')
print('\n--E) Teste da tamanhoMaiorString -- ')
print('\nLISTA:')
print(lst)
maiorSt=  tamanhoMaiorString (lst) 
if maiorSt != None:
    print(f'\nO tamanho da maior string da lista é {maiorSt}')
else:
    print('\nNão há strings na lista')
    
print('\nLISTA:')
lx=[10,[60,70,[78,9.6]],6,7]
print(lx)
maiorSt=  tamanhoMaiorString (lx) 
if maiorSt != None:
    print(f'\nO tamanho da maior string da lista é {maiorSt}')
else:
    print('\nNão há strings na lista')    