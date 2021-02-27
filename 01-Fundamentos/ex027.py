# DESAFIO 028: Faça um programa que leia o nome de uma pessoa, mostrando em seguida o primeiro e último nome
# separadamente.

nome = str(input('\nDigite seu nome completo: ')).strip()
dividido = nome.split()

print('Primeiro nome: {}'.format(dividido[0]))
print('Último nome: {}'.format(dividido[len(dividido)-1]))
