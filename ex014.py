# DESAFIO 014: 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para
# graus Fahrenheit.

print('CONVERSOR DE TEMPERATURAS')

graus_celsius = float(input('Temperatura em °C: '))
conversao = (((9 * graus_celsius) / 5) + 32)
graus_fahrenheit = conversao

print('Temperatura em °F: {}'.format(conversao))
