# DESAFIO 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

nome = str(input('\nDigite seu nome completo: ')).strip()
havename = 'SILVA' in nome.upper().split()

print('Seu nome tem Silva? {}'.format(havename))
