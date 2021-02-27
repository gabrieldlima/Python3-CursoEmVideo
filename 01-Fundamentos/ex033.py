# DESAFIO 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('\nDigite três valores:')

n1 = int(input('Primeiro valor >>> '))
n2 = int(input('Segundo valor >>> '))
n3 = int(input('Terceiro valor >>> '))
valores = [n1, n2, n3]
crescente = sorted(valores)

print('\nAnalisando os valores digitados temos:')
print('O menor valor é o {}.'.format(crescente[0]))
print('O maior valor é o {}.'.format(crescente[2]))
