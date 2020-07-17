# DESAFIO 084: Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A - Quantas pessoas foram cadastradas.
# B - Uma listagem com as pessoas mais pesadas.
# C - Uma listagem com as pessoas mais leves.

group = list()
people = list()
weight0 = list()
weight1 = list()
count_people = 0
higher = 0
lowest = 0

while True:
    people.append(str(input('Nome: ')).strip().capitalize())
    people.append(float(input('Peso: ')))
    group.append(people[:])
    count_people += 1
    people.clear()
    answer = str(input('Quer continuar?[S/N] ').strip().upper())
    if answer == 'N':
        break

for weight in range(len(group)):
    if weight == 0:
        higher = group[weight][1]
        lowest = group[weight][1]
    else:
        if group[weight][1] > higher:
            higher = group[weight][1]
        if group[weight][1] < lowest:
            lowest = group[weight][1]

for name in range(len(group)):
    if higher in group[name]:
        (weight1.append(group[name][0]))
    if lowest in group[name]:
        (weight0.append(group[name][0]))

print(f'Ao todo foram cadastradas {count_people} pessoas.\n'
      f'O maior peso foi de {higher}Kg. Peso de: {weight1}\n'
      f'O menor peso foi de {lowest}Kg. Peso de: {weight0}')
