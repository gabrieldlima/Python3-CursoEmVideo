# DESAFIO 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá
# perguntar se o usuário que ou não continuar. No final, mostre:
# A - Quantas pessoas tem mais de 18 anos.
# B - Quantos homens foram cadastrados.
# C - Quantas mulheres tem menos de 20 anos

print('{:-^50}'.format(' CADASTRO PESSOAL '))

sex = carry_on = ''
count_people_18 = count_man = count_woman_20 = 0

while True:
    age = int(input('\nIDADE: '))
    if age >= 18:
        count_people_18 += 1

    sex = str(input('SEXO[M/F]: ')).upper().strip()[0]
    while sex not in 'FM':
        print('INVÁLIDO! Tecle M ou F.')
        sex = str((input('SEXO[M/F]: '))).upper().strip()[0]
    if sex == 'M':
        count_man += 1
    if sex == 'F' and age >= 20:
        count_woman_20 += 1
    carry_on = str(input('Quer continuar a cadastrar mais pessoas[S/N]? ')).upper().strip()[0]

    while carry_on not in 'SN':
        print('INVÁLIDO! Tecle S ou N.')
        carry_on = str(input('Quer continuar a cadastrar mais pessoas[S/N]? ')).upper().strip()
    if carry_on == 'N':
        break

print(f'\nAnalisando as pessoas cadastradas, temos que:\n'
      f'- {count_people_18} pessoas tem mais de 18 anos.\n'
      f'- {count_man} homens foram cadastrados.\n'      
      f'- {count_woman_20} mulheres têm mais de 20 anos\n')
