# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:33:17 2026

@author: joisa
"""

# As funções solicitadas nesse exercício devem funcionar para qualquer 
# lista de pessoas com a estrutura descrita, não somente para a lista 
# do exemplo do bloco principal

# Considere uma lista em que cada elemento é uma lista com as 
# seguintes informações de uma pessoa: 
# nome completo, estado de nascimento (sigla) e data de nascimento
#(string no formato dd/mm/aaaa)


# A) Escreva uma função  (exibeFormatado) que 
# receba uma lista de pessoas como a descrita e para cada pessoa na lista 
# exiba em uma linha o nome da pessoa no formato UltimoNome, PrimeiroNome 
# seguido da data de nascimento com o mês por extenso.
# Por exemplo, para o primeiro elemento da lista fornecida 
# no BP deveria ser exibido
# oliveira, lala - 21 de setembro de 2004

# B) Escreva uma função (exibeTabFreqMesNasc) que receba a lista 
# de pessoas e exiba o nome de cada mes seguido da quantidade de 
# pessoas nascidas nesse mes


# C) Escreva uma função (criaTabFreqEstado) que receba a lista 
# de pessoas e crie e retorne uma nova lista em que cada elemento é 
# [estado, quantidade de pessoas desse estado]
# OBS: será necessário fazer uma busca na lista em construção. Pra isso 
# faça uma função de busca separada




lpessoas= [
    ['lala lobo oliveira', 'RJ', '21/09/2004'],
    ['buba carneiro pereira', 'RJ', '32/12/1983'],
    ['lele monte oliveira', 'RO', '18/03/1963'],
    ['dada carvalho', 'SP', '12/05/2012'],
    ['buba lobo ponte', 'MG', '26/05/2002'],
    ['gege carvalho', 'MT', '10/11/2003'],
    ['tata falcao ponte', 'RJ', '02/09/1988'],
    ['vivi pedras carvalho', 'SC', '17/08/1993'],
    ['vava carvalho', 'SC', '19/01/1954'],
    ['caca leao pereira', 'PR', '28/01/1997'],
    ['lulu carneiro macieira', 'PA', '13/10/1993'],
    ['dede leao vale pereira', 'RJ', '10/12/2001'],
    ['tita branco carvalho', 'SC', '12/01/1974'],
    ['tito coelho pereira', 'MA', '22/05/2007'],
    ['zaza branco macieira', 'AM', '14/06/1989'],
    ['tete coelho pereira', 'MA', '23/02/2013']
    ]

