# DESAFIO 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno rentagular
# (largura e altura) e mostre a área do terreno.


def area(h, w):
    a = h * w
    print(f'A area de {h}x{w} é de {a:.2f}m².')


print(f'{" CONTROLE DE TERRENOS ":-^40}')

height = float(input('ALTURA: '))
widht = float(input('LARGURA'))
area(height, widht)
