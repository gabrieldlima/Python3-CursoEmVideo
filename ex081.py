# DESAFIO 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A - Quantos números foram digitados.
# B - A lista de valores, ordenada de forma decrescente.
# C - Se o valor 5 foi digitado e está ou não na lista.

number_list = list()

while True:
    number = int(input('Digite um número: '))
    if number not in number_list:
        number_list.append(number)
    else:
        print('Valor já digitado!')

    answer = str(input('Quer continuar a digitar números[S/N]? ')).upper().strip()[0]
    if answer == 'N':
        break

number_list.sort(reverse=True)
print(f'Ao todo foram digitados {len(number_list)} números.\n'
      f'A lista de números em ordem decrescente é: {number_list}')
if 5 in number_list:
    print(f'O número 5 apareceu {number_list.count(5)} vezes.')
