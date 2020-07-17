# DESAFIO 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
option = ''

while option != 5:

    print('=-=' * 10)
    print('[1] - SOMAR\n'
          '[2] - MULTIPLICAR\n'
          '[3] - MAIOR\n'
          '[4] - NOVOS NÚMEROS\n'
          '[5] - SAIR DO PROGRAMA')
    option = int(input('Qual a sua opção? '))

    if option == 1:
        sum = (n1 + n2)
        print('{} + {} = {}'.format(n1, n2, sum))

    elif option == 2:
        multiply = (n1 * n2)
        print('{} x {} = {}'.format(n1, n2, multiply))

    elif option == 3:
        if n1 > n2:
            bigger_number = n1
            print('O maior número é o {}.'.format(bigger_number))
        elif n2 > n1:
            bigger_number = n2
            print('O maior número é o {}.'.format(bigger_number))

    elif option == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif option > 5:
        print('Opção inválida! Tente novamente')

    sleep(0.35)

print('FINALIZANDO...')
sleep(0.7)
print('=-=' * 10)
print('FIM DO PROGRAMA! VOLTE SEMPRE!')
