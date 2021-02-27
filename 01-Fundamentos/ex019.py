# DESAFIO 019: Um professor quer sortear um dos seus alunos para apagar o quadro. Faça um programa que ajude ele, lendo
# o nome dos alunos e escrevendo na tela o nome dos escolhidos.

from random import choice

print('\nQUEM É O ESCOLHIDO?')

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
nomes = (n1, n2, n3, n4)
sorteado = choice(nomes)

print('O aluno escolhido foi {}'.format(sorteado))
