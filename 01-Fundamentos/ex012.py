# DESAFIO 012: Faça um algoritimo que leia o preço de um produte e mostre seu novo preço, com 5% de desconto.

product = str(input('NOME DO PRODUTO: ')).strip()
price = float(input('PREÇO DO PRODUTO: R$'))
new_price = price - (price * 5 / 100)

print('NOVO PREÇO COM 5% DE DESCONTO: R${:.2f}'.format(new_price))
