# DESAFIO 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto com parâmetro e mostre uma
# mensagem com tamanho adaptável. Exemplo:
# escreva('Olá, Mundo!')
# -------------
#  Olá, Mundo
# -------------


def write(msg):
    size = len(msg) + 4
    print('-' * size)
    print(f'  {msg}  ')
    print('-' * size)


txt = str(input('Digite um frase: ')).strip()
write(txt)
