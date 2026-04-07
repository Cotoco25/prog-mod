# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:07:37 2026

@author: joisa
"""

def calcula_media_ponderada(n1,n2,n3,p1,p2,p3):
    medPond= (p1*n1 + p2*n2 + p3*n3)/(p1+p2+p3)
    return medPond
    


def calcula_nota_final(pv1,t1a,t1b,pv2,t2a,t2b,trab):
    g1= calcula_media_ponderada(pv1,t1a,t1b,2,1,1)
    g2= calcula_media_ponderada(pv2,t2a,t2b,5,2,3)
    print(f'Grau1:{g1:.1f}')
    print(f'Grau2:{g2:.1f}')
    nf= calcula_media_ponderada(g1,g2,trab,1,2,2)
    return nf 


#BP
pv1= float(input('Nota da prova do Grau1:'))
teste1a=float(input('Nota do teste A do Grau1:'))
teste1b= float(input('Nota do teste B do Grau1:'))
pv2= float(input('Nota da prova do Grau2:'))
teste2a=float(input('Nota do teste A do Grau2:'))
teste2b= float(input('Nota do teste B do Grau2:'))
trabalho= float(input('Nota do trabalho:'))

notaFinal= calcula_nota_final(pv1,teste1a,teste1b,pv2,teste2a,teste2b,trabalho)
if notaFinal >= 5.0:
    print(f'Nota final: {notaFinal:.1f} - APROVADO')
elif notaFinal >= 3.0:
    print(f'Nota final: {notaFinal:.1f} - Faz Prova Final')
else:
    print(f'Nota final: {notaFinal:.1f} - REPROVADO')