# DESAFIO 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média
# de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

count_age = 0
older_man = 0
name_older_man = ''
count_woman_younger = 0

for people in range(1, 5):
    name = str(input('Informe o {}º nome: '.format(people))).strip()

    age = int(input('Informe a idade dessa pessoa: '))
    count_age += age

    sex = str(input('Informe o seu sexo(M/F): ')).upper().strip()
    print('')
    if sex == 'M':
        if people == 1:
            older_man = age
            name_older_man = name
        if age > older_man:
            older_man = age
            name_older_man = name

    if sex == 'F':
        if age < 20:
            count_woman_younger += 1

average_age = (count_age / 4)

print('Analisando este grupo de pessoas, temos que:')
print('- A média de idade do grupo é de {} anos.'.format(average_age))
print('- O homem mais velho se chama {} e tem {} anos'.format(name_older_man.title(), older_man))

if count_woman_younger < 2:
    print('- Ao todo, somente {} mulher tem menos de 20 anos.'.format(count_woman_younger))
if count_woman_younger >= 2:
    print('- Ao todo, {} mulheres tem menos de 20 anos.'.format(count_woman_younger))
