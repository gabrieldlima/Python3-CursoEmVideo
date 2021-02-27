# DESAFIO 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre sua hipotenusa.

print('TEOREMA DE PITÁGORAS')

ca = float(input('Cateto Adjacente >>> '))
co = float(input('Cateto Oposto >>> '))
hipotenusa = ((ca ** 2) + (co ** 2)) ** (1/2)

print('Hipotenusa >>> {:.1f}'.format(hipotenusa))
