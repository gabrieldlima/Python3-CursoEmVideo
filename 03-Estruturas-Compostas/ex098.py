# DESAFIO 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo
# e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
# A- De 1 até 10, de 1 em 1.
# B- De 10 até 0, de 2 em 2.
# C- Uma contagem personalizada.

from time import sleep


def count(start, end, step):
    print(f'Contagem de {start} até {end} de {step} em {step}:')

    if step == 0:
        step = 1

    if start < end:
        if step < 0:
            step *= -1
        for c in range(start, end + step, step):
            print(c, end=' ')
            sleep(0.4)
        print()

    elif start > end:
        if step > 0:
            step = -step
        for c in range(start, end - 1, step):
            print(c, end=' ')
            sleep(0.4)
        print()
    print('=-=' * 15)


count(1, 10, 1)
count(10, 0, 2)

print('Agora é sua vez de personalizar a contagem!')
START = int(input('Ínicio: '))
END = int(input('Final: '))
STEP = int(input('Passo: '))
count(START, END, STEP)
