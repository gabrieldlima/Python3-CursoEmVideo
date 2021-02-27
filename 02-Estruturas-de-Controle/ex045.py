# DESAFIO 045: Crie um programa que faça o computador jogor Jokenpô com você.

from random import choice
from time import sleep

print('\033[1;35m-=' * 4)
print('JOKENPÔ')
print('-=' * 4)

pedra = 1
papel = 2
tesoura = 3
cpuoptions = (pedra, papel, tesoura)
cpuchoice = choice(cpuoptions)
player = int(input('FAÇA SUA JOGADA:\n'  # JOGADOR ESCOLHE SUA JOGADA.
                   '[ 1 ] --- PEDRA\n'
                   '[ 2 ] --- PAPEL\n'
                   '[ 3 ] --- TESOURA\n'
                   'DIGITE SUA OPÇÃO >>> '))

print('       JO   ')
sleep(0.5)
print('       KEN   ')
sleep(0.5)
print('       PÔ   ')

if cpuchoice == 1:  # COMPUTADOR ESCOLHE 'PEDRA'
    if player == 1:
        print('\nPEDRA contra PEDRA')
        print('\033[1;94m--- EMPATE! -----\033[m')
    elif player == 2:
        print('\nPAPEL contra PEDRA')
        print('\033[1;32m---- VITÓRIA! ----\033[m')
    elif player == 3:
        print('\nTESOURA contra PEDRA')
        print('\033[1;91m---- DERROTA! ----\033[m')

elif cpuchoice == 2:  # COMPUTADOR ESCOLHE 'PAPEL'.
    if player == 1:
        print('\nPEDRA contra PAPEL ')
        print('\033[1;91m---- DERROTA! ----\033[m')
    elif player == 2:
        print('\nPAPEL contra PAPEL')
        print('\033[1;94m--- EMPATE! -----\033[m')
    elif player == 3:
        print('\nTESOURA contra PAPEL')
        print('\033[1;32m---- VITÓRIA! ----\033[m')

elif cpuchoice == 3:  # COMPUTADOR ESCOLHE 'TESOURA'.
    if player == 1:
        print('\nPEDRA contra TESOURA')
        print('\033[1;32m---- VITÓRIA! ----\033[m')
    elif player == 2:
        print('\nPAPEL contra TESOURA')
        print('\033[1;91m---- DERROTA! ----\033[m')
    elif player == 3:
        print('\nTESOURA contra TESOURA')
        print('\033[1;94m--- EMPATE! -----\033[m')
