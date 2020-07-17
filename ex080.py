# DESAFIO 080: Crie um programa onde o usário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
# posição correta de inserção(sem usar o sort()). No final, mostre a lista ordenada na tela.

number_list = list()
for c in range(0, 5):
    number = int(input(f'Digite o {c + 1}º número: '))
    if c == 0 or number > number_list[-1]:
        number_list.append(number)
    else:
        pos = 0
        while pos < len(number_list):
            if number <= number_list[pos]:
                number_list.insert(pos, number)
                break
            pos += 1
print(f'Números digitados em ordem crescente: {number_list}')
