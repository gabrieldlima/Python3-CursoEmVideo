# DESAFO 066: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles(desconsiderando o flag).

count = 0
sum_of_number = 0

while True:
    number = int(input('Digite um número[999 para parar]: '))
    if number == 999:
        break
    sum_of_number += number
    count += 1
print(f'A soma dos {count} valores digitados foi igual à: {sum_of_number}')
