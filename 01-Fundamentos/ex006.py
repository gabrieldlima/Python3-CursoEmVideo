# DESAFIO 006: Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

number = int(input('Digite um número: '))
print('Analizando o número digitado: ')

double = (number * 2)
triple = (number * 3)
square_root = sqrt(number)

print('O seu dobro é {}\n'
      'O seu  triplo é {}\n'
      'A sua raíz de é {:.0f}'.format(double, triple, square_root))
