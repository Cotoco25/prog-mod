# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

def substituiVogais(palavra, NovoCaractere):
    ns = ""
    for carac in palavra:
        if carac in "aeiouAEIOU":
            ns = ns +NovoCaractere
        else:
            ns = ns + carac
    return ns


novaSt = substituiVogais("salsicha e bolacha", "X")
print(novaSt)

def exibeStRec(s):
    if s == "":
        return
    print(s[0])
    exibeStRec(s[1:]) 

#a funcao tira a primeira letra da string e é a chama novamente
#sempre tirando a primeira letra e printando ela ate a string ser ""


novaString = exibeStRec("MAR")
print(novaString)

def exibeStRecInvertido(s):
    if s == "":
        return
    exibeStRec(s[1:])
    print(s[0])
    
novaStringInversa = exibeStRec("MAR")
print(novaStringInversa)


def contaCaracteresRec(s):
    if s == "":
        return 0
    qtdRestante = contaCaracteresRec(s[1:])
    return 1 + qtdRestante


conta = contaCaracteresRec("palavra")
print(conta)

