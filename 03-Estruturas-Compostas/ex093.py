# DESAFIO 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa var ler o nome do jo-
# gador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
# será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

data = dict()
data['nome'] = str(input('Nome do jogador: ')).strip().title()
matches = int(input(f'Quantas partidas {data["nome"]} jogou? '))

if matches != 0:
    data['gols'] = []
    for c in range(matches):
        data['gols'].append(int(input(f'- Quantos gols na {c + 1}º partida? ')))
    data['total'] = sum(data['gols'][:])
print('-=-' * 18)

print(data)
print('-=-' * 18)

for k, v in data.items():
    print(f'O campo {k} tem o valor {v}')
print('-=-' * 18)

print(f'O jogador {data["nome"]} jogou {matches} partidas:')
for v in range(0, len(data['gols'])):
    print(f'    => Na partida {v + 1}, fez {data["gols"][v]} gols.')
print(f'Foi um total de {data["total"]} gols.')
