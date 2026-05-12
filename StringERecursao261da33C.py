# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:34:52 2026

@author: PC-PROF
"""

# Escreva uma função recursiva, denominada exibeStRec, 
# que receba uma string e exiba cada caractere em 
# uma linha

def exibeStRec(s):
    if s == '':   # CASO BASE
        return  
    print(s[0])
    exibeStRec(s[1:])
     
def outraExibeStRec(s):   #exibe invertida 
    if s == '':   # CASO BASE
        return  
    outraExibeStRec(s[1:]) 
    print(s[0])

# Escreva uma função recursiva que retorne 
# a quantidade de caracteres de uma string
# recebida. (Não use len)
def contaCaracteresRec(s):
    if s=='':
        return 0
    return 1 + contaCaracteresRec(s[1:])

# Escreva uma função recursiva que retorne 
# a quantidade de vogais de uma string
# recebida. (Não use len)

# Escreva uma função RECURSIVA, denominada substituiVogaisRec,
# que  receba uma string e um caractere e construa e retorne 
# uma nova string com todas as vogais da string original  
# substituídas pelo caractere recebido 
# OBS: substitui não é um BOM nome, pois não é possível 
# fazer  substituições na string recebida
# STRING é IMUTÁVEL 

#BP
outraExibeStRec('MAR')
print(f'Quantidade de caracteres em MAR: {contaCaracteresRec("MAR")}')

