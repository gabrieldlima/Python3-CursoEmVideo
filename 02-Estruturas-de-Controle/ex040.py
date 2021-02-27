# DESAFIO 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de
# acordo com a média atingida:
# Média abaixo de 5.0: Reprovado
# Média entre 5.0 e 6.9: Recuperacão
# Média 7.0 ou superior: Aprovado

print('=' * 17)
print('MÉDIA ARITIMÉTICA')
print('=' * 17)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = ((nota1 + nota2) / 2)

if media < 5.0:
    print('Média: {:.2f}\n'
          'Reprovado!'.format(media))

elif media >= 5.0 and media <= 6.9:
    print('Média: {:.2f}\n'
          'Recuperação!'.format(media))

elif media > 7.0:
    print('Média: {:.2f}\n'
          'Aprovado!'.format(media))
