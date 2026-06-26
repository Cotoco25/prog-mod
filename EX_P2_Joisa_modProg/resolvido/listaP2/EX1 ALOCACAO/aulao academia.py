# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 18:29:54 2026

@author: guilh
"""

def criaListaVaga():
    lista = []
    arq = open('salascomvagas.txt', 'r')
    for item in arq:
        item = item.rstrip()
        lista.append(int(item))
    arq.close()
    return lista

def criaListaProf():
    lista = []
    arq = open('professores.txt', 'r')
    for item in arq:
        item = item.rstrip()
        lista.append(item)
    arq.close()
    return lista

def exibeSalas(Vagas,Profs, x):
    print(x)
    print('='*30)
    for i in range(len(Vagas)):
        print(f'SALA:{i+1} - Prof:{Profs[i]} - Vagas:{Vagas[i]}')
    print()

def alocacao(Vagas, Profs):
    print('--------- ALOCACAO ---------')
    arq = open('turmas.txt', 'r')
    for item in arq:
        item = item.rstrip()
        item = item.split(',')
        cod = item[0]
        qtd = int(item[1])
        prof = item[2]
        if prof in Profs:
            num = Profs.index(item[2])
            if qtd<=int(Vagas[num]):
                Vagas[num] = Vagas[num]-qtd
                print(f'Turma:{cod} - Prof:{prof} - Sala:{num+1}')
            else:
                print(f'Turma:{cod} - Prof:{prof} - QtdAl:{qtd}- Sala:NÃO ALOCADA')
    arq.close()
        

Vagas = criaListaVaga()
Profs = criaListaProf()

exibeSalas(Vagas,Profs, 'ANTES DA ALOCACAO:')
print()
alocacao(Vagas, Profs)
print()
exibeSalas(Vagas,Profs, 'DEPOIS DA ALOCACAO:')
