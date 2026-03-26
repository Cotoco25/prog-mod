# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:48:01 2026

@author: PC34
"""

#definir funcao que recebe 6003 segundos e retorna horas, minutos e segundos.


def representacao_horario(temposeg):
    totmin = temposeg//60
    qtdseg = temposeg%60
    qtdhoras = totmin//60
    qtdmin = totmin%60
    
    s=f'{qtdhoras:2d}h:{qtdmin:2d}m:{qtdseg:2d}s'
    return s

tempototseg = int(input('Entre o tempo total em segundos:'))
sthorario = representacao_horario(tempototseg)
print(f'{tempototseg} segundos corresponde a {sthorario}')