# DESAFIO 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pesoas ainda não
# antingiram a maioridade e quantas já são maiores.

from datetime import datetime

ano_atual = datetime.today().year
maioridade_true = 0
maioridade_false = 0

for pessoas in range(1, 8):

    nascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(pessoas)))
    idade = (ano_atual - nascimento)

    if idade >= 21:
        maioridade_true += 1

    elif idade < 21:
        maioridade_false += 1

print('De acordo com o nascimento das pessoas acima:'
      '\n- {} já possuem maioridade'
      '\n- {} ainda não atingiram a maioridade'.format(maioridade_true, maioridade_false))
