# DESAFIO 089: Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No
# final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno in-
# dividualmente.

print(f'{" LANÇAMENTO DE NOTAS ":•^50}')

students_list = list()
students_temp = list()
average = list()

while True:
    students_temp.append(str(input('Nome: ')).strip().capitalize())
    students_temp.append(float(input('Nota 1: ')))
    students_temp.append(float(input('Nota 2: ')))
    average.append((students_temp[:][1] + students_temp[:][2]) / 2)
    students_list.append(students_temp[:])
    students_temp.clear()
    answer = str(input('Quer continuar? [S/N] ')).strip().upper()
    if answer == 'N':
        break

print(f'{" BOLETIM DA CLASSE ":-^30}')
print(f'{"Nº"}| {"NOME":^15} | {"MÉDIA":>8}')

for people in range(len(students_list)):
    print(f'{people} | {students_list[people][0]:^15} | {average[people]:>8.1f}')

print('-' * 30)
print('•' * 50)

while True:
    note = int(input('Mostrar notas de qual aluno?[999 to Stop] '))
    if note != 999:
        for aluno in range(1):
            print(f'Notas de {students_list[note][0]}: {students_list[note][1:]}')
            print('.' * 50)
    elif note == 999:
        break

print(f'{" VOLTE SEMPRE ":•^50}')
