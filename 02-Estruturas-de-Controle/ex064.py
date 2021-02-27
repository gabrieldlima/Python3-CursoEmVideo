# DESAFIO 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é condição de parada. No final, mostre quantos números foram digitados e qual foi a soma en-
# tre eles (desconsiderando o flag).

number = sum_of_number = number_counter = 0

while number != 999:
    number = int(input('Digite um valor [999 para parar]: '))
    if number != 999:
        sum_of_number += number
        number_counter += 1

print('\nVocê digitou {} números e a soma entre eles é igual à: {}'.format(number_counter, sum_of_number))
