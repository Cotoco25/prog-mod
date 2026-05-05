# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 15:41:50 2022

@author: Joísa
"""
def ehVogal(carac):
    return carac in 'aeiouAEIOU'

def ehLetra(carac):
    return ('a'<=carac and carac <='z') or ('A'<=carac and carac<='Z')
   
def ehLetra2(carac):
    return   'a'<=carac<='z' or'A'<=carac<='Z'

def ehConsoante(carac):
    return ('a'<=carac<='z' or'A'<=carac<='Z') and carac not in 'aeiouAEIOU'

def ehConsoante2(carac):
    return ehLetra(carac) and not ehVogal(carac)

def ehMaiuscula(carac):
    return 'A'<=carac<='Z'

def ehMinuscula(carac):
    return 'a'<=carac<='z'

def ehDigito(carac):
    return '0'<=carac<='9'

def converteMinMaiusc(carac):
    if ehMinuscula(carac):
        codMaiusc= ord(carac) - (ord('a')-ord('A'))
        maiuscula = chr(codMaiusc)
        return maiuscula
    else:
        return carac
    
def converteMaiuscMin(carac):
    if ehMaiuscula(carac):
        codMinusc= ord(carac) + (ord('a')-ord('A'))
        minuscula = chr(codMinusc)
        return minuscula
    else:
        return carac

print('------ehVogal-------')
print(ehVogal('E'))
print(ehVogal('u'))
print(ehVogal('d'))
print('------ehLetra-------')
print(ehLetra('T'))
print(ehLetra('+'))
print('------ehConsoante-------')
print(ehConsoante('f'))
print(ehConsoante('o'))
print(ehConsoante('G'))
print('------ehConsoante2-------')
print(ehConsoante2('f'))
print(ehConsoante2('o'))
print(ehConsoante2('G'))
print('------ehMaiuscula-------')
print(ehMaiuscula('f'))
print(ehMaiuscula('F'))
print('------ehMinuscula-------')
print(ehMinuscula('f'))
print(ehMinuscula('F'))
print('------ehDigito-------')
print(ehDigito('a'))
print(ehDigito('2'))
print(ehDigito('0'))
print('------converteMinMaiusc-------')
print(converteMinMaiusc('d'))
print(converteMinMaiusc('t'))
print(converteMinMaiusc('+'))
print(converteMinMaiusc('R'))
print('------converteMaiuscMin-------')
print(converteMaiuscMin('P'))
print(converteMaiuscMin('A'))
print(converteMaiuscMin('x'))