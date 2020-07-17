# DESAFIO 037: Escreva um programa em python que leia um número inteiro qualquer e peça para o usuário escolher qual
# será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('\nDigite um número inteiro: '))
conversao = int(input(('''Opções de conversão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL
>>> ''')))

if conversao == 1:
    print('{} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))

elif conversao == 2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))

elif conversao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))

else:
    print('Opção inválida! Tente novamente.')
