# DESAFIO 036: Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. Pergunte o valor da
# casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
# então o emprestimo sera negado.

print('+' * 32)
print('APROVAÇÃO DE EMPRESTIMO BANCÁRIO')
print('+' * 32)

valorcasa = float(input('\nValor do imovél: R$'))
salario = float(input('Renda salárial: R$'))
pagamentoanos = int(input('Quantos anos de financiamento: '))

condicaosalarial = (salario * 30 / 100)
parcelas = (pagamentoanos * 12)
prestacaomensal = (valorcasa / parcelas)

if prestacaomensal <= condicaosalarial:
    print('\nEmprestimo Aprovado!\n'
          'Parcela fixa de R${:.3f} dividido em {} meses sem juros.'.format(prestacaomensal, parcelas))

elif prestacaomensal > condicaosalarial:
    print('\nEmprestimo Negado!\n'
          'O valor da parcela excedeu 30% do valor de seu salário.')
