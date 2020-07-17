# DESAFIO 090: Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário. No
# final, mostre o conteúdo da estrutura na tela.

student = dict()
student['nome'] = str(input('Nome: ')).strip().capitalize()
student['média'] = float(input('Média: '))

if student['média'] >= 7:
    student['situação'] = 'APROVADO'
elif 5 <= student['média'] < 7:
    student['situação'] = 'RECUPERAÇÃO'
else:
    student['situação'] = 'REPROVADO'

print('=-=' * 10)
for k, v in student.items():
    print(f'- {k} é igual à {v}')
