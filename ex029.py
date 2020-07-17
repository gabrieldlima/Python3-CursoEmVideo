# DESAFIO 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensangem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

print('\nRadar Eletrônico')

velocidade = int(input('\nVelocidade atual do carro >>> '))
multa = ((velocidade - 80) * 7)

if velocidade > 80:
    print('\nMulta por velocidade acima de *80km/h\nTaxa da multa: R$7.00 por Km ultrapassado\nTotal: R${:.2f}'
          .format(multa))

else:
    print('Dirija com cidado! Tenha um bom dia.')
