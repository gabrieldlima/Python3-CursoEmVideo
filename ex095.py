# DESAFIO 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

team = list()
player = dict()
matches = list()

while True:

    player.clear()
    player['nome'] = str(input('Nome do Jogador: ')).strip().title()
    matches_total = int(input(f'Quantas partidas {player["nome"]} jogou? '))
    matches.clear()
    for c in range(0, matches_total):
        matches.append(int(input(f'  Quantos gols na partida {c + 1}? ')))
    player['gols'] = matches[:]
    player['total'] = sum(matches)
    team.append(player.copy())
    while True:
        proceed = str(input('Quer continuar[S/N]? ')).strip().upper()
        if proceed in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if proceed == 'N':
        break

print('-' * 40)
print('cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

for k, v in enumerate(team):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)

while True:
    search = int(input('Mostrar dados de qual jogador[999 para parar]? '))
    if search == 999:
        break
    if search >= len(team):
        print(f'ERRO! Não existe o jogodor com o códigi {search}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {team[search]["nome"]}:')
        for i, g in enumerate(team[search]['gols']):
            print(f' --> No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
