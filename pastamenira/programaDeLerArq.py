# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 11:42:58 2026

@author: PC45
"""

arq = open('nomes.txt','r')
arqSaida = open('carneirocoelho.txt', 'w')

for linha in arq:
    linha = linha.strip()
    if 'carneiro' in linha or 'coelho' in linha:
        arqSaida.write(linha+'\n') # +'\n' para fazer linhas entre os carneiros
    print(linha)

arq.close()
arqSaida.close()