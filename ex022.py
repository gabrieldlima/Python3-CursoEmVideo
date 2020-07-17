# DESAFIO 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiscúlas e minisculas;
# Quantas letras tem sem considerar os espaços;
# Quantas letras tem o primeiro nome;

nome = str(input('\nDigite seu nome completo: ')).strip()

print('\nNome em maiscúlas: {}'.format(nome.upper()))
print('Nome em minuscúlas: {}'.format(nome.lower()))

dividido = nome.split()
letrastotal = nome.replace(' ', '')

print('Números de letras no nome: {}'.format(len(letrastotal)))
print('Número de letras do primeiro nome: {}'.format(len(dividido[0])))
