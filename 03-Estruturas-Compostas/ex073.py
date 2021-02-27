# DESAFIO 073: Crie um tupla preechida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na
# ordem de colocação. Depois mostre:
# A - Os 5 primeiros times;
# B - Os últimos 4 colocados;
# C - Times em ordem alfabética.
# D - Em que posição está o time da Chapecoense.

print('=' * 50)
print('{:-^50}'.format(' TABELA DO BRASILEIRÃO '))
print('=' * 50)

team_tuple = ('Flamengo', 'Palmeiras', 'Santos', 'Corinthians', 'São Paulo',
              'Grêmio', 'Bahia', 'Internacional', 'Goiás', 'Atlético Paranaense',
              'Vasco da Gama', 'Atlético Mineiro', 'Botafogo', 'Fluminense', 'Fortaleza',
              'Ceará', 'CSA', 'Cruzeiro', 'Avaí', 'Chapecoense')

print('{:.^50}.'.format('PRIMEIROS COLOCADOS'))
for pos, team in enumerate(team_tuple):
    if pos < 5:
        print(f'{pos + 1}º - {team}')

print('{:.^50}'.format('ÚLTIMOS COLOCADOS'))
count = 16
for team in team_tuple[-4:]:
    count += 1
    print(f'{count}º - {team}')

print('{:.^50}'.format('TIMES EM ORDEM ALFABÉTICA'))
alphabetical_order = sorted(team_tuple)
for team in alphabetical_order:
    print(f'{team}')

print(f'\nO time da Chapecoense está na {team_tuple.index("Chapecoense") + 1}º posição.')
