# DESAFIO 057: Faça um programa que leia o sexo de uma pessoa, mas só aceire os valores 'M' ou 'F'. Caso esteja errado,
# peça a digiação novamente até ter um valor correto.

types_sex = ('M', 'F')
sex = str(input('Informe o sexo do usuário [M/F]: ')).upper().strip()

while sex not in types_sex:
    sex = str(input('Dados inválidos. Tente novamente: ')).upper().strip()
print('Sexo registrado com sucesso.')
