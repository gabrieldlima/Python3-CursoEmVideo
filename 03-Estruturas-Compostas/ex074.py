# DESAFIO 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a
# listagem de números gerados e também o menor e o maior valor que estão na tupla.

from random import randint

numbers = (randint(0, 5), randint(0, 5), randint(0, 5),
           randint(0, 5), randint(0, 5))

print('Os números sorteados foram: ', end='')
for n in numbers:
    print(f'{n}', end=' ')

print(f'\nO maior valor digitado foi {max(numbers)}.\n'
      f'O menor valor sorteado foi {min(numbers)}.')
