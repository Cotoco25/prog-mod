# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 18:59:18 2026

@author: guilh
"""

#arq= open('funcionarios.txt' , 'r') #nome, horas trabalhadas mensal, departamento, anos na empresa
#departamento, valor da hora

def criaListaDepValorHo():
    listaNova = []
    departamento = open('departamentos.txt' , 'r')
    for linha in departamento:
        linha = linha.rstrip()
        valor = linha.split(",")
        valor[1] = float(valor[1])
        lista = [valor[0],valor[1]]
        listaNova.append(lista)
    departamento.close()
    return listaNova

def obtemValorHoraDep(lista, dep):
    for value in lista:
        if type(value) == list:
            lista1 = value
            if dep in lista1:
                return lista1[1]
    return 5

def exibePagamentos(lista):
    func = open('funcionarios.txt', 'r')
    cont = 0
    for linha in func:
        linha = linha.rstrip()
        valor = linha.split(',')
        valor[1] = float(valor[1])
        valor[3] = float(valor[3])
        b = obtemValorHoraDep(lista,valor[2])
        soma = (valor[1] * b) + (350 * (valor[3]//3))
        print(f'Func: {valor[0]} - Pagamento: R$:{soma:.2f}')
        cont+=soma
    func.close()
    return f'O valor total em pagamentos no mês é R${cont:.2f}'


#BP
letraA = criaListaDepValorHo()
print(letraA)
print(obtemValorHoraDep(letraA, "MARKETING"))
print()
print(exibePagamentos(letraA))