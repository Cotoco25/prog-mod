# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:33:29 2026

@author: PC-PROF
"""

# Escreva uma funcao que receba 
# uma lista e remova todas as ocorrencias 
# de string no primeiro nivel da lista
def eliminaSimples(ls):
    ind=0
    while ind<len(ls):
        if type(ls[ind]) == str:
            ls.remove(ls[ind])    # o indice não pode avancar 
        else:
            ind+=1 

# Escreva uma funcao RECURSIVA que receba 
# uma lista e remova todas as ocorrencias 
# de string em qq nivel da lista
def eliminaRec(ls):
    ind=0
    while ind<len(ls):
        if type(ls[ind]) == str:
            ls.remove(ls[ind])    # o indice não pode avancar 
        else:
            if type(ls[ind]) == list:
                eliminaRec(ls[ind])
            ind+=1 

#BP
lx=['ar','eu',13,37,'oi',77,['mel','ri',19],'sol','mar',88,'ui']

print(lx)
eliminaRec(lx)
print(lx)