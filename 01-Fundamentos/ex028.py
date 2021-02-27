# DESAFIO 028: Escreva um programa que faça o computador 'pensar' em número entre 0 e 5 e peça para o úsuario tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o úsuario venceu ou
# perdeu.

from random import randint
from time import sleep

print('\033[1;94m+=+\033[m' * 21)
print('\033[1;94;mTENTE ADIVINHAR O NÚMERO ENTRE 0 E 5 QUE O COMPUTADOR ESCOLHEU!')
print('\033[1;94m+=+\033[m' * 21)

computer = randint(0, 5)
player = int(input('\n\033[1;94mQUAL FOI O NÚMERO? >>> \033[m'))

print('\033[1;94mPROCESSANDO...\033[m')
sleep(0.8)

if player == computer:
    print('\033[1;92mPARABÉNS!!! O NÚMERO ESCOLHIDO FOI O {}.'.format(computer))

elif player != computer:
    print('\033[1;31mOPS... VOCÊ ERROU! O NÚMERO ESCOLHIDO FOI O {}.\033[m'.format(computer))
