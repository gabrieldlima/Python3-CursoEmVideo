# DESAFIO 103: Faça um programa que tenha um função chamada ficha(), que receba dois parâmetros opcionais: o nome do jo-
# gador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não 
# tenha sido informado corretamente.

def token(player='<unknown>', goals=0):
    print(f'O jogador {player} fez {goals} gols no campeonato.')


name = str(input('Nome do jogador: ')).strip().capitalize()
number_goals = str(input('Número de gols: ')).strip()

if number_goals.isnumeric():
    number_goals = int(number_goals)
else:
    number_goals = int(0)

if name == '':
    token(goals=number_goals)
else:
    token(name, number_goals)
