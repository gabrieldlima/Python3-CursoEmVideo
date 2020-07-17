# DESAFIO 077: Crie um programa que tenha uma tupa com várias palavras (não usar acentos). Depois disso, você deve mos-
# trar cada palavra, quais são as suas vogais.

words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
         'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
         'TRABALHAR', 'MERCADO', 'PROGRAMADOS', 'FUTURO')

for pos in range(0, len(words)):
    print(f'\nNa palavra {words[pos]} tem as vogais: ', end='')

    for letter in words[pos]:
        if letter in 'AEIOU':
            print(f'{letter}', end=' ')
