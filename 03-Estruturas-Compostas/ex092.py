# DESAFIO 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um
# dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

data = dict()
data['nome'] = str(input('Nome: ')).strip().title()
data['nascimento'] = int(input('Ano de Nascimento: '))
age = datetime.now().year - data['nascimento']
data['idade'] = age
ctps = int(input('Carteira de trabalho (0 não tem): '))

if ctps != 0:
    data['ctps'] = ctps
    data['contratação'] = int(input('Ano de contratação: '))
    data['sálario'] = float(input('Sálario: R$'))
    data['aposentadoria'] = data['idade'] + ((data['contratação'] + 35) - datetime.now().year)

print('-=-' * 10)
for k, v in data.items():
    print(f'- {k} tem o valor {v}')
print('-=-' * 10)
