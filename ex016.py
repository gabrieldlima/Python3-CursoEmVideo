# DESAFIO 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira.

from math import trunc

number = float(input('Digite um número Real(Ex: 2.759): '))
porcaointeira = trunc(number)

print('A porção inteira de {} é igual a {}.'.format(number, porcaointeira))
