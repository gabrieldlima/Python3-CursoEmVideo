# DESAFIO 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

total_divisoes = 0
numero = int(input('Digite um número: '))

for c in range(1, numero + 1):
    if numero % c == 0:
        total_divisoes = total_divisoes + 1

if total_divisoes == 2:
    print('{} é um número primo.'.format(numero))
elif total_divisoes > 2:
    print('{} não é um número primo.'.format(numero))
