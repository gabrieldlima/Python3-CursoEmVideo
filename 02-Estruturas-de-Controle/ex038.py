# DESAFIO 038: Escreva um programa que leia dois números interios e compare-os, mostrando na tela um mensagem:
# O primeiro valor é maior;
# O segundo valor é maior;
# Não existe valor maior, os dois são iguais;

print('\nQUAL É O MAIOR VALOR?')
n1 = int(input('\nPrimeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print('O primeiro valor é o maior.')
elif n1 < n2:
    print('O segundo valor é o maior.')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais.')
