# DESAFIO 039: Faça um programa que leia o ano de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

print('=' * 19)
print('ALISTAMENTO MILITAR')
print('=' * 19)

nome = str(input('Nome completo: ')).strip()
nascimento = int(input('Ano de nascimento: '))
sexo = str(input('Sexo(M/F): ')).strip().upper()
anoatual = date.today().year
idade = (anoatual - nascimento)

if sexo == 'M':
    if idade == 18:
        print('Você tem 18 anos, já é hora de se alistar!')

    elif idade < 18:
        restante = (18 - idade)
        print('Ainda não está na hora de alistar! Restam {} anos.'.format(restante))

    elif idade > 18:
        passou = (idade - 18)
        print('Você deveria ter se alistado a {} anos, aliste imediatamente!'.format(passou))

elif sexo == 'F':
    print('Você não precisa fazer o alistamento militar obrigatório.')
