# DESAFIO 048: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se
# encontram no intervalo de 1 até 500.

acumulador = 0
contador = 0

for c in range(1, 501, 2):
    if c % 2 != 0 and c % 3 == 0:
        contador += 1
        acumulador += c

print('A soma dos {} valores solicitados é igual a {}.'.format(contador, acumulador))
