# DESAFIO 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre na tela a sua categoria:
# -Até 9 anos: MIRIM
# -Até 14 anos: INFANTIL
# -Até 19 anos: JÚNIOR
# -Até 25 anos: SÊNIOR
# -Acima de 25 anos: MASTER

from datetime import date

print('=' * 21)
print('CLASSIFICANDO ATLETAS')
print('=' * 21)

nascimento = int(input('Ano de nascimento: '))
anoatual = date.today().year
idade = (anoatual - nascimento)
print('\nIdade do atleta: {} anos'.format(idade))

if idade <= 9:
    print('Categoria: MIRIM')

elif 9 < idade <= 14:
    print('Categoria: INFANTIL')

elif 14 < idade <= 19:
    print('Categoria: JÚNIOR')

elif 19 < idade <= 25:
    print('Categoria: SÊNIOR')

elif idade > 25:
    print('Categoria: MASTER')
