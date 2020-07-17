# DESAFIO 031: Denselvolva um programa que pergunte a distância de um viagem em Km. Calcule o preço da passagem,
# cobrando R$0.50 por Km para viagens de até 200km e R$0.40 para viagens mais longas.

distancia = int(input('\nDistância da viagem em Km: '))

if distancia <= 200:
    passagem1 = distancia * 0.50
    print('Valor total da passagem: R${:.2f}'.format(passagem1))

elif distancia > 200:
    passagem2 = distancia * 0.45
    print('Valor total da passagem: R${:.2f}'.format(passagem2))

else:
    print('Opção inválida! Tente novamente.')
