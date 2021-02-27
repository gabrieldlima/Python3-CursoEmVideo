# DESAFIO 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastra-os em uma lista. Caso o
# número já exista lá dentro, ele não será adicionado. No final, serão exibidos os valores únicos digitadados, em ordem
# crescente.

number_list = list()
carry_on = 'S'
while True:

    while carry_on == 'S':
        number = (int(input('Digite um número: ')))

        if number not in number_list:
            number_list.append(number)
            print('Valor adicionado com sucesso...')
        else:
            print('Valor duplicado! Não vou adicionar...')

        carry_on = str(input('Quer continuar? ')).upper().strip()[0]

        while carry_on not in 'SN':
            print('Inválido! Tente novamente digitando S ou N.')
            carry_on = str(input('Quer continuar? ')).upper().strip()[0]

    if carry_on == 'N':
        break

number_list.sort()
print(f'Você digitou os valores: {number_list}')
