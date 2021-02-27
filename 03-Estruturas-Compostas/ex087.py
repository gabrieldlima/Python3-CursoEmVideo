# DESAFIO 087: Aprimore o desafio anterior, mostrando no final:
# A - A soma de todos os valores pares digitedos.
# B - A soma dos valores da terceira coluna.
# C - O maior valor da segunda linha.

print(f'{" MATRIZ 3x3 ":•^45}')

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even = 0
line2 = list()
column3 = list()

for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))

        if matrix[line][column] % 2 == 0:
            even += matrix[line][column]

        if column == 2:
            column3.append(matrix[line][column])

        if line == 1:
            line2.append(matrix[line][column])

print('•' * 45)
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[line][column]:^5}] ', end='')
    print()

print('•' * 45)
if even > 0:
    print(f'A soma dos valores pares é {even}.')
print(f'A soma dos valores da terceira coluna é {sum(column3)}.')
print(f'O maior valor da segunda linha é {max(line2)}.')
