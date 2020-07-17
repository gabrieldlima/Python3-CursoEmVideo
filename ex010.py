# DESAFIO 010: Crie um programa que leia quanto de dinheiro um pessoa tem na carteira e mostre quantos dólares ela pode
# comprar.

print('{:-^50}'.format('CONVERSOR DE MOEDAS'))

money = float(input('Quantos reais você pretende gastar: R$'))
dolar = 4.06  # VAlOR DE DÓLAR EM 10/05/2019
total_dolar = (money / dolar)

print('Com R${:.2f} você pode comprar: U${:.2f}'.format(money, total_dolar))
