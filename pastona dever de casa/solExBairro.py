# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:00:08 2026

@author: PC-PROF
"""
# OBJ: criar e retornar lsita em q cada elem é [bairro, prM2]

# antes, criar lista de somadores, cada elem é [bairro,totArea,totPr]

def buscaNaLstSomadores(lsomadores,bairroProc):
    for ind,el in enumerate(lsomadores):
        if el[0] == bairroProc:
            return ind 
    return -1 

def criaListaPrMQ(limoveis):
    
    lsomadores = [ ]
    
    for imovel in limoveis:
        bairro = imovel[0]
        area= imovel[1]
        pr= imovel[2]
        ind= buscaNaLstSomadores(lsomadores,bairro)
        if ind != -1: 
            lsomadores[ind][1]+=area
            lsomadores[ind][2]+=pr
        else: 
            lsomadores.append([bairro,area,pr])
    lprM2=[]
    for el in lsomadores:
        lprM2.append([el[0] , el[2]/el[1]])
    
    return lprM2
    
#BP
limov= [ ['botafogo',120,900000], ['leblon',100,3300000], ['copacabana',90,1200000],
  ['botafogo',80,1100000], ['botafogo',80,800000], ['copacabana',60,1000000],
  ['leblon',60,2400000], ['copacabana',130,2600000],
  ['gloria',70,700000], ['flamengo',80,800000], ['gloria',60,70000],
  ]

lBairroPrM2= criaListaPrMQ(limov)
print(lBairroPrM2)