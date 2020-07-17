# DESAFIO 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantida-
# de de tinta necessária para pintá-la, sabendi que cada litro de tinta pinta uma área de 2 metros quadrados.

print('===CALCULO DE ÁREA PARA PINTURA===')

height = float(input('ALTURA: '))
width = float(input('LARGURA: '))
area = (height * width)
ink = (area / 2)

print('ÁREA TOTAL: {}m²\n'.format(area))
print('UM LITRO DE TINTA PINTA UMA ÁREA DE 2m²')
print('LITROS DE TINTA NECESSÁRIOS: {}L'.format(ink))
