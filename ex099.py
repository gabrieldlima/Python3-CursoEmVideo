# DESAFIO 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def bigger(*numbers):
    print('Analisando os valores passados...')
    print(*numbers, sep=', ', end=' >>> ')
    print(f'Foram informados {len(numbers)} valores ao todo.')
    print(f'O maior valor digitado foi o {max(numbers)}.')
    print('=-=' * 20)


bigger(2, 9, 4, 5, 7, 1)
bigger(4, 7, 0)
bigger(1, 2)
bigger(6)
bigger(0)
