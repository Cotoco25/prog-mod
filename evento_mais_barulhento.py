# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:53:35 2026

@author: PC37
"""

def calculaNivelRuido(rBase,k,p):
    rTotal = rBase+k*p*(p-1)
    return rTotal

def eventoMaisBarulhento(r1,k1,p1,r2,k2,p2):
    print("Evento A:")
    print(f"Nivel de ruido total estimado: {calculaNivelRuido(r1,k1,p1):.2f} db")
    if calculaNivelRuido(r1,k1,p1)>130:
        print("BARULHO EXCESSIVO!!")
    print()
    print("Evento B:")
    print(f"Nivel de ruido total estimado: {calculaNivelRuido(r2,k2,p2):.2f} db")
    if calculaNivelRuido(r2,k2,p2)>130:
        print("BARULHO EXCESSIVO!!")
    if calculaNivelRuido(r1,k1,p1)>calculaNivelRuido(r2,k2,p2):
        print("O evento A é mais barulhento que o evento B.")
    else:
        print("O evento B é mais barulhento que o evento A.")

print("--- TESTE 1 ---")
eventoMaisBarulhento(5,0.05,40,20,0.08,30)
print()
print(30*"-")
print()
print("--- TESTE 2 ---")
eventoMaisBarulhento(10,0.07,60,10,0.05,15)