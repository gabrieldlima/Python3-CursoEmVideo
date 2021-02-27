# DESAFIO 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de
# uma Sequência de Fibonacci. Fn = Fn - 1 + Fn - 2

print('Sequência de Fibonacci')

n_terms = int(input('Quantos termos você quer ver? '))
term1 = 0
term2 = 1
print('{} → {} → '.format(term1, term2), end='')
count = 3

while count <= n_terms:
    term3 = (term1 + term2)
    term1 = term2
    term2 = term3
    print('{} → '.format(term3), end='')
    count += 1
print('FIM')
