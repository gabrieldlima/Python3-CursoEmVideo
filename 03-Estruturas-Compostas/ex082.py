# DESAFIO 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras
# que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo
# das três listas geradas.

numbers_list = list()
carry_on = ''
even = list()
odd = list()

while True:

    numbers = int(input('Digite um número: '))
    if numbers not in numbers_list and numbers != 0:
        print('Valor adicionado com sucesso!')
        numbers_list.append(numbers)
    else:
        print('Valores já digitados não serão adicionados!')

    carry_on = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    while carry_on not in 'SN':
        print('Inválido! Digite S ou N.')
        carry_on = str(input('Quer continuar?[S/N] ')).upper().strip()[0]

    if carry_on == 'N':
        break

for pos, n in enumerate(numbers_list):

    if n % 2 == 0:
        even.append(n)

    else:
        odd.append(n)

print(f'Você digitou os números: {numbers_list}\n'
      f'Os números pares foram: {sorted(even)}\n'
      f'Os números ímpares foram: {sorted(odd)}')
