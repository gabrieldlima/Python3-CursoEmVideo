# DESAFIO 034: Escreva um programa que pergunte o sálario de uma funcionário e calcule o valor do seu aumento. Para
# salários superiores a R$1250.00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('\nSalário do funcionário: R$'))

if salario > 1250.00:
    aumento = salario + (salario * 10 / 100)
    print('O novo salário com 10% de aumento passa a ser: R${:.2f}'.format(aumento))

elif salario <= 1250.00:
    aumento = salario + (salario * 15 / 100)
    print('O novo salário com 15% de aumento passa a ser: R${:.2f}'.format(aumento))
