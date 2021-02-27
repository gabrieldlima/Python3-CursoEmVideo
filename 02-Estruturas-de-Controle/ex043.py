# DESAFIO 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu índice de massa corporal(IMC)
# e mostre seu status, de acordo com a tabela abaixo:
# -Abaixo de 18.5: Abaixo do peso
# -Ente 18.5 e 25: Peso ideal
# -25 até 30: Sobrepeso
# -30 até 40: Obesidade
# -Acima de 40: Obesidade Mórbida

print('\nÍNDICE DE MASSA CORPORAL')

peso = float(input('\nSeu peso: '))
altura = float(input('Sua altura: '))
imc = (peso / (altura ** 2))

print('\nSeu IMC: {:.1f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')
