# DESAFIO 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[0:5].lower() == 'santo')
