# DESAFIO 085: Crie um programa ondo o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

numberlist = [[], []]

for n in range(7):
    number = int(input(f'Digite o {n + 1}º número: '))
    if number % 2 == 0:
        numberlist[0].append(number)
    else:
        numberlist[1].append(number)

print(f'Os números pares digitados foram: {sorted(numberlist[0])}')
print(f'Os números ímpares digitados foram: {sorted(numberlist[1])}')
