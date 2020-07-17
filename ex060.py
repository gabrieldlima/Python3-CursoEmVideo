# DESAFIO 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

number = int(input('Digite um número para ver o seu fatorial: '))
factorial = 1

for c in range(number, 1, -1):
    factorial = factorial * c
print('O fatorial de {} é igual à {}.'.format(number, factorial))
