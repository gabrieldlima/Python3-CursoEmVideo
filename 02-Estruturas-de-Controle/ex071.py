# DESAFIO 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual
# será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('=' * 50)
print('{:-^50}'.format(' BANCO CURSO EM VÍDEO '))
print('=' * 50)

value = int(input('Qual valor você deseja sacar? R$'))
total = value
ballot = 50
total_ballot = 0
while True:
    if total >= ballot:
        total -= ballot
        total_ballot += 1
    else:
        if total_ballot > 0:
            print(f'Total de {total_ballot} cédulas de {ballot}.')
        if ballot == 50:
            ballot = 20
        elif ballot == 20:
            ballot = 10
        elif ballot == 10:
            ballot = 1
        total_ballot = 0
        if total == 0:
            break

print('=' * 50)
print('Volte Sempre!!! BANCO CEV')
