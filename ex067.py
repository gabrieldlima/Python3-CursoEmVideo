# DESAFIO 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo
# usuário. O programa será interrompido quando o número solicitado for negativo.

print('{:~^40}'.format(' GERADOR DE TABUADA '))

while True:
    number = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 35)
    if number < 0:
        break
    for c in range(1, 11):
        print(f'{number} X {c} = {number * c}')
    print('-' * 35)

print('FIM DO PROGRAMA! VOLTE SEMPRE!')
