# DESAFIO 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A - Quantas vezes apareceu o valor 9.
# B - Em que posição foi digititado o primeiro valor 3.
# C - Quais foram os números pares.

numbers = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))

print(f'Você digitou os números: {numbers}')
print(f'- O número 9 apareceu {numbers.count(9)} vezes.')

if 3 in numbers:
    print(f'- O número 3 apareceu primeiro na {numbers.index(3) + 1}º posição.')
else:
    print(f'- Não foi digitado o valor 3.')

print(f'- Os números pares foram: ', end='')
for n in numbers:
    if n % 2 == 0:
        print(f'{n}', end=' ')
