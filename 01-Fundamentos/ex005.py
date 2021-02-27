# DESAFIO 005: Faça um programa que leia um número inteiro e mostre na tela seu sucessor e antecessor.

number = int(input('Digite um número inteiro: '))
sucessor = (number + 1)
predecessor = (number - 1)

print('Sucessor: {}\nAntecessor: {}'.format(predecessor, sucessor))
