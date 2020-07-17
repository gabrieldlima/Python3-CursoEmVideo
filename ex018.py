# DESAFIO 018: Faça um programa que leia  um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse
# ângulo.

from math import radians, sin, cos, tan

print('\nTRIÂNGULO RETÂNGULO')

angulo = float(input('Valor do angulo: '))
radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print('Seno >>> {:.2f}\nCosseno >>> {:.2f}\nTangente >>> {:.2f}'.format(seno, cosseno, tangente))
