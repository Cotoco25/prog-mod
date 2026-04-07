# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 21:24:29 2025

@author: joisa
"""

import math

def quantasDeUmTipo(totGarrafas, capCaixa):
    return math.ceil(totGarrafas/capCaixa)

def custoTotalDeUmTipo(qtdCaixas, precoUnit):
    return qtdCaixas*precoUnit

#Bloco Principal
totalGarrafas = int(input('Total de garrafas a serem transportadas:'))
capBasica = int(input('Capacidade da caixa basica:'))
precoBasica=  float(input('Preco unitario da caixa basica:'))
capReforcada = int(input('Capacidade da caixa reforcada:'))
precoReforcada=  float(input('Preco unitario da caixa reforcada:'))

qtBasica= quantasDeUmTipo(totalGarrafas,capBasica)
prTotBasica= custoTotalDeUmTipo(qtBasica,precoBasica)

qtRef= quantasDeUmTipo(totalGarrafas,capReforcada)
prTotRefor= custoTotalDeUmTipo(qtRef,precoReforcada)

print(f'Basica:  {qtBasica} caixas- preco total R${prTotBasica:.2f}')
print(f'Reforçada:  {qtRef} caixas- preco total R${prTotRefor:.2f}')