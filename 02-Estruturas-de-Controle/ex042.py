# DESAFIO 042: Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será
# formado:
# -Equilátero: todos os lados iguais;
# -Isósceles: dois lados iguais, um diferente;
# -Escaleno: todos os lados diferentes;

print('\nANALISADOR DE TRIÂNGULOS')

seg1 = float(input('\nPrimeiro segmento de reta: '))
seg2 = float(input('Segundo segmento de reta: '))
seg3 = float(input('Terceiro segmento de reta: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('\nAnalisado os valores formamos um:')
    if seg1 == seg2 and seg2 == seg3:
        print('-Triângulo Equilátero')
    elif seg1 != seg2 and seg2 != seg3 and seg3 != seg1:
        print('-Triâgulo Escaleno')
    else:
        print('-Triângulo Isósceles')
else:
    print('Não é possivel se formar um triângulo!')
