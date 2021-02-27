# DESAFIO 088: Faça um programa que ajude um jogodor da MEGA SENA a criar palpites. O programa vai perguntar quantos jo-
# gos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

print(f'{" JOGO DA MEGA SENA ":•^45}')

games = int(input('Quantos jogos você quer que eu sortei? '))
listsort1 = list()
listsort2 = list()
count = 0

for c in range(games):
    for x in range(6):
        listsort2.append(randint(0, 61))
    listsort1.append(listsort2[:])
    listsort2.clear()

print(f'{" SORTEANDO JOGOS ":•^45}')

for item in range(len(listsort1)):
    print(F'JOGO {item + 1}: {sorted(listsort1[item])}')
    sleep(0.7)

print(f'{" BOA SORTE! ":•^45}')
