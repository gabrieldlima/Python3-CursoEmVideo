# DESAFIO 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e sua
# condição de pagamento:
# -à vista dinheiro/cheque >>> 10% de desconto
# -à vista no cartão: 5% de desconto
# -em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros

print('GERENCIADOR DE PAGAMENTOS')

preco = float(input('\nPreço do produto: R$'))
pagamento = int(input('Forma de pagamento:\n'
                      '[ 1 ] --- À vista no dinheiro/cheque\n'
                      '[ 2 ] --- À vista no cartão\n'
                      '[ 3 ] --- Parcelado\n'
                      'Digite a opção escolhida: '))

if pagamento == 1:
    novopreco = (preco - (preco * 10 / 100))
    print('\nNovo preço com 10% de desconto: R${:.2f}'.format(novopreco))

elif pagamento == 2:
    novopreco = (preco - (preco * 5 / 100))
    print('Novo preço com 5% de desconto: R${:.2f}'.format(novopreco))

elif pagamento == 3:
    parcelas = int(input('Nº de parcelas: '))
    if parcelas <= 2:
        print('Preço normal de R${}\nParcelas:{}x de R${:.2f}'.format(preco, (preco / parcelas), parcelas))

    elif parcelas >= 3:
        novopreco = (preco + (preco * 20 / 100))
        parcelamensal = (novopreco / parcelas)
        print('Novo preço em {}x(juros de 20%): R${:.2f}\n'
              'Parcelas: {}x de R${:.2f}'.format(parcelas, novopreco, parcelas, parcelamensal))
