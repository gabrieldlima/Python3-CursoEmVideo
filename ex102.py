# DESAFIO 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o nú-
# mero a calcular e outro chamado show(), que será um valor lógico (opcional) indincando se será mostrado ou não na tela
# o processo de cálculo do fatorial.

def factorial(num, show=False):
    fac = 1
    for c in range(num, 0, -1):
        if show == True:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        fac = fac * c
    return fac


num = int(input('Digite um número para ver seu fatorial: '))
print(factorial(num, show=True))
