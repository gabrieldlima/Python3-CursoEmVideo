# DESAFIO 091: Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados
# em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no
# dado.

from random import randint
from time import sleep
from operator import itemgetter

players = dict()

print(f'{" JOGAR OS DADOS ":=^45}')
for c in range(4):
    players[f'jogador{c + 1}'] = randint(1, 6)

print('Valores sorteados:')
for k, v in players.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.9)

print(f'{" RAKING DOS JOGADORES ":=^45}')
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
for indice, valor in enumerate(ranking):
    print(f'{indice + 1}º Lugar: {valor[0]} com {valor[1]}')
    sleep(0.9)
