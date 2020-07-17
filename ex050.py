# DESAFIO 050: Densenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

acumulador = 0

for c in range(1, 7):
    numero = int(input('Digite o {}° valor: '.format(c)))
    if numero % 2 == 0:
        acumulador += numero

print('A soma dos números pares dessa lista é igual a {}.'.format(acumulador))
