# DESAFIO 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiro
# termos dessa progressão.
# # an = a1 + (n – 1) * r

a1 = int(input('\nPrimeiro termo da P.A: '))
razao = int(input('Razão da P.A: '))
decimo = a1 + (10 - 1) * razao

for c in range(a1, decimo + razao, razao):
    print('{}'.format(c), end=', ')
print('...')
