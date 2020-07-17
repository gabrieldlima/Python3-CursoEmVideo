# DESAFIO 013: Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('SALÁRIO DO FUNCIONÁRIO: R$'))
increase = salary + (salary * 15 / 100)

print('NOVO SALÁRIO COM 15% DE AUMENTO: R${:.2f}'.format(increase))
