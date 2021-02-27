# DESAFIO 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No
# final, mostre a matriz na tela, com a formatação correta.

print(f'{" MATRIZ 3x3 ":=^30}')
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for line in range(3):
    for column in range(3):
        matrix[line][column] = int(input(f'Digite um valor para [{line}, {column}]: '))

print('=' * 30)
for line in range(3):
    for column in range(3):
        print(f'[{matrix[line][column]:^5}]', end='')
    print()
