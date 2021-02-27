# DESAFIO 058: Melhore o jogo do DESAFIO 028 onde o computador vai penser em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites forma necessários para vencer.

from random import randint

print('JOGO DA ADIVINHAÇÃO\n')

computer_choice = randint(0, 10)
player_choice = int(input('Tente adivinhar o número escolhido pelo computador.\n'
                          'Este número está entre 0 e 5:\n'
                          '>>> '))
count_tries = 1

while player_choice != computer_choice:

    count_tries = count_tries + 1
    if player_choice < computer_choice:
        player_choice = int(input('Mais... Tente de novo.\n'
                                  '>>> '))
    elif player_choice > computer_choice:
        player_choice = int(input('Menos... Tente de novo.\n'
                                  '>>> '))

print('Parabéns! Você acertou o número escolhido.\n'
      'Foram necessárias {} tentativas para vencer.'.format(count_tries))
