# DESAFIO 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase0 = str(input('Digite um frase qualquer:\n>>> ')).lower().strip()
frase1 = frase0.replace(' ', '')
frase_inverso = frase1[::-1]

print('Analisando a frase de trás para frente, temos que:')

if frase_inverso == frase1:
    print('A frase digitada é um palíndromo.')
elif frase_inverso != frase1:
    print('A frase digitada não é um palíndromo.')
