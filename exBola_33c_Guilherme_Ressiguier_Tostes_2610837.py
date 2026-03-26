#   NOME: Guilherme R R Tostes
#   MAT: 2610837
#   33C
#   Prof: Josia
#   Exercicio: Exercicio Bola

import math




def calc_cubo(lado):
    volumecubo = (lado**3)
    return volumecubo


def calc_esfera(r):
    volumeesfera = (4/3)*math.pi*r**3
    return volumeesfera


lado = float(input('entre o valor do lado do cubo: '))
r = lado/4



vol_esfera_finalizado = calc_esfera(r)
print (vol_esfera_finalizado)


vol_cubo_finalizado = calc_cubo(lado)
print (vol_cubo_finalizado)


def espaco_vazio(lado,r):
    vazio = calc_cubo(lado)-(calc_esfera(r)*8)
    return vazio

espaco_vazio_total = espaco_vazio(lado,r)
print (espaco_vazio_total)

print("Um cubo com lado de ",lado,"cm tem volume",espaco_vazio_total,"de espaco vazio total.")

