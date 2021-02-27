# DESAFIO 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.

name = str(input('Digite seu nome: ')).title().strip()
print('Olá {}, seja bem-vindo!'.format(name))
