# DESAFIO 072: Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

tuple_number = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                'treze','catorze ', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    number = int(input('Digite um número entre 0 e 20: '))
    if 0 <= number <= 20:
        break
    else:
        print('Inválido! Tente novamente.', end=' ')

for pos, items in enumerate(tuple_number):
    if number == pos:
        print(f'Você digitou o número {items}.')
