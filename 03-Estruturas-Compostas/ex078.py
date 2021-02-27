# DESAFIO 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior
# e o menor valor digitado e as suas respectivas posições na lista.

number_list = list()
for number in range(5):
    number_list.append(int(input(f'Digite o {number + 1} número: ')))
higher = max(number_list)
lowest = min(number_list)
h_pos = list()
l_pos = list()

for pos, n in enumerate(number_list):
    if number_list[pos] == higher:
        h_pos.append(pos + 1)
    elif number_list[pos] == lowest:
        l_pos.append(pos + 1)

print(f'Você digitou os valores: {number_list}')
print(f'O maior valor digitado foi {higher} nas posiçãos {h_pos}')
print(f'O menor valor digitado foi {lowest} nas posiçãos {l_pos}')
