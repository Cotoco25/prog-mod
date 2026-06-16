# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 00:22:41 2025

@author: joisa
"""

lsignos= ['Macaco','Galo','Cao','Porco','Rato','Boi',
          'Tigre','Coelho','Dragao','Cobra','Cavalo','Carneiro']

lcont= [0]*12  # so serve para lista de contadores

arq= open('dadospessoas.txt','r')

for linha in arq:
    linha= arq.readline()
    lst= linha.strip().split(';')
    ano= int(lst[1][-4:])
    #print(ano,'=>',end='')
    indice= ano%12
    #print(lsignos[indice])
    lcont[indice]+=1 

#print(lcont)
arq.close()
# EXIBIR A TABELA:
print('\nSigno e quantidade de pessoas do signo')
for ind,signo in enumerate(lsignos):
    print(f'{signo} - {lcont[ind]}')


    