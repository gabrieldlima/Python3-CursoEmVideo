# DESAFIO 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de um PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura while.
# an = a1 + (n – 1) * r

print('GERADOR DE PROGRESSÃO ARITIMÉTICA\n')

a1 = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
term = a1
cont = 1

while cont <= 10:
    print('{}'.format(term), end=' ')
    term += reason
    cont += 1
