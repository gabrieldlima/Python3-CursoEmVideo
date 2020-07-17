# DESAFIO 014: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de
# dias que pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por
# Km rodado.

print('Diária do carro: R$60.00\nKm rodados: R$0.15')

alugueldias = int(input('Quantidades de dias alugado: '))
kmpercorridos = float(input('Quantidade de km percorridos: '))
diaria = (alugueldias * 60)
km = (kmpercorridos * 0.15)

print('Total: R${:.2f}'.format(diaria + km))
