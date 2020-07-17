# DESAFIO 035: Densenvolva um programa que leia o comprimento de três retas e diga ao usuário se podem ou não formar um
# triângulo.

x1 = float(input('\nPrimeiro seguimento de reta: '))
x2 = float(input('Segundo seguimento de reta: '))
x3 = float(input('Terceiro seguimento de reta: '))

if (x2 - x3) < x1 < (x2 + x3) and (x3 - x1) < x2 < (x3 + x1) and (x1 - x2) < x3 < (x1 + x2):
    print('\nÉ POSSÍVEL formar um triângulo.')

else:
    print('\nNÃO É POSSÍVEL formar um triângulo.')
