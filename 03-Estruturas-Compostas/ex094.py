# DESAFIO 094: Crie um progama que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre:
# A - Quantas pessoas foram cadastradas.
# B - A média de idade.
# C - Uma lista com as mulheres.
# D - Uma lista de pessoas com idade acima da média.

ddictionary = dict()
llist = list()
womans = list()
count_ages = 0

while True:

    print('-=-' * 10)
    while True:
        name = str(input('Nome: ')).strip().title()
        if len(name) < 3:
            print('INVÁLIDO! O nome deve ter no mínimo 3 caracteres.')
        if len(name) >= 3:
            ddictionary['nome'] = name
            break

    while True:
        sex = str(input('Sexo[M/F]: ')).strip().upper()
        if sex not in 'MF':
            print('INVÁLIDO! Por favor, digite apenas M ou F.')
        elif len(sex) == 0:
            print('INVÁLIDO! Por favor, digite apenas M ou F.')
        else:
            ddictionary['sexo'] = sex
            break

    while True:
        age = int(input('Idade: '))
        if age == 0:
            print('INVÁLIDO! Idade deve ser maior que 0.')
        elif age > 100:
            print('INVÁLIDO! Idade deve ser menor que 100.')
        else:
            ddictionary['idade'] = age
            count_ages += age
            break

    if sex == 'F':
        womans.append(ddictionary['nome'])

    llist.append(ddictionary.copy())
    ddictionary.clear()

    while True:
        proceed = str(input('Quer continuar[S/N]? ')).strip().upper()
        if proceed not in 'SN':
            print('INVÁLIDO! Responda apenas S ou N.')
        elif len(proceed) == 0:
            print('INVÁLIDO! Responda apenas S ou N.')
        else:
            break
    if proceed == 'N':
        break

average = (count_ages / len(llist))

print(f'A) Ao todo temos {len(llist)} pessoas.\n'
      f'B) A média de idade é de {average:.2f} anos.\n'
      f'C) As mulheres cadastradas foram: {womans}\n'
      f'D) Lista de pessoas que estão acima da média:')

for i in range(len(llist)):
    if llist[i]['idade'] > average:
        print(f'- Nome: {llist[i]["nome"]}; Sexo: {llist[i]["sexo"]};  Idade: {llist[i]["idade"]};')
