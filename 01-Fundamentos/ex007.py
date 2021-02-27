# DESAFIO 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('{:-^25}'.format('MÉDIA ARITIMÉTICA'))

note1 = float(input('Primeira nota: '))
note2 = float(input('Segunda nota: '))
average = ((note1 + note2) / 2)

print('Total: {:.1f}'.format(average))
