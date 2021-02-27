# DESAFIO 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador
# PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('{:-^35}'.format('JOGO DE PAR OU ÍMPAR'))
total = 0
answer = ''
count_victory = 0

while True:
    computer_choice = randint(0, 10)
    player_choice = int(input('Escolha um número: '))
    answer = str(input('Par ou Ímpar[P/Í]: ')).strip().upper()
    total = (computer_choice + player_choice)

    while answer not in 'PI':
        answer = str(input('Par ou Ímpar[P/Í]: ')).strip().upper()

    print(f'Você jogou {player_choice} e o computador {computer_choice} | total → {computer_choice + player_choice}')
    print('DEU PAR.' if total % 2 == 0 else 'DEU ÍMPAR.')

    if total % 2 == 0:
        if answer == 'P':
            count_victory += 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    elif total % 2 != 0:
        if answer == 'I':
            count_victory += 1
        else:
            print('VOCÊ PERDEU!!!')
            break
    print('VOCÊ VENCEU!!! VAMOS JOGAR NOVAMENTE...\n')

print(f'\nGAME OVER!!! Você venceu {count_victory} vezes.')
