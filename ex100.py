# DESAFIO 100: Faça um programa que tenha um lista chamada números e duas funções chamadas sorteia() e somaPar(). A pri-
# meira vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os va-
# lores PARES sorteados pela funçao anterior.

from random import randint
from time import sleep


def raffle(list_num):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(5):
        list_num.append(randint(1, 10))
        print(list_num[c], end=' ')
        sleep(0.3)
    print()


def sum_even(list_num):
    count = 0
    for value in list_num:
        if value % 2 == 0:
            count += value
    print(f'Somando os valores pares de {list_num}, temos {count}.')


numbers = list()
raffle(numbers)
sum_even(numbers)
