# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

def perc2(s):
    for elem in s:
        print(elem)
        
        
perc2('ALHURES')


def achaPosicao(palavra, letra):
    n = len(palavra)
    for i in range(n):
        if palavra[i] == letra:
            return i
    return -1


print(achaPosicao("banana", "n"))



def contaCaractere(palavra, letra):
    n = len(palavra)
    soma = 0
    for i in range(n):
        palavra[i]
        if palavra[i] == letra:
            soma +=1
    return soma


print(contaCaractere("banana", "a"))

s = "BRAS"
for x in enumerate(s):
    print(x)

print()

d = "BRAS"
for pos,elem in enumerate(d):
    print(pos,"",elem)
    
    
print()

#aqui: enumerate
def achaPosicaoVS2(t,caracDesejado):
    for pos,elem in enumerate(t):
        if elem == caracDesejado:
            return pos
    return -1

print(achaPosicaoVS2("banana","a"))



list(range(10,20,3))


g = 'ALHURES'

g[1:4] # =LHU
g[:2] # = AL
g[4:] # = RES
g[1:6:2] # = LUE