# DESAFIO 070: Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:
# A - Qual é o total gasto na compra.
# B - Quantos produtos custam mais de R$1000.
# C - Qual é o nome do produto mais barato.

print('{:-^50}'.format(' TABELA DE COMPRAS '))

total = product_1000 = cont = product_low = 0
product_cheap = ''

while True:
    product_name = str(input('\nNome do Produto: ')).strip().upper()

    price = float(input('Preço do Produto: R$ '))
    if price > 1000:
        product_1000 += 1
    total += price
    cont += 1
    if cont == 1 or price < product_low:
        product_low = price
        product_cheap = product_name

    carry_on = str(input('Quer continuar a comprar? ')).upper().strip()[0]
    while carry_on not in 'SN':
        print('INVÁLIDO! Tecle S ou N.')
        carry_on = str(input('Quer continuar a comprar? ')).upper().strip()[0]
    if carry_on == 'N':
        break

print('====== CUMPUM FISCAL ======')
print(f'Total da compra: R${total:.2f}\n'
      f'Produto mais barato: {product_cheap}\n'
      f'Produtos com valor maior de R$1000.00: {product_1000}\n')
