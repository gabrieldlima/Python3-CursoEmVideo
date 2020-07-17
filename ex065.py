# DESAFIO 065: Crie um programa que leia vários números pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valor dos valores lidos. O programa deve perguntar ao usuário se ele quer ou
# não continuar a digitar valores.

more_number = 'S'
sum_of_number = count_number = higher = lower = 0

while more_number in 'Ss':
    number = int(input('Digite um número: '))
    sum_of_number += number
    count_number += 1
    if count_number == 1:
        higher = number
        lower = number
    else:
        if number > higher:
            higher = number
        if number < lower:
            lower = number
    more_number = str(input('Quer continuar[S/N]? ')).upper().strip()[0]

average = (sum_of_number / count_number)
print('A média dos {} os valores digitados foi de {}\n'
      'O maior valor foi {} e o menor foi {}.'.format(count_number, average, higher, lower))
print('\nFIM')
