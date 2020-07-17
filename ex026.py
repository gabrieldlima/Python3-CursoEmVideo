# DESAFO 027: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra 'A', em que
# posição ela apareçe pela primeira vez e em que posição ela aparece a última vez.

frase = str(input('\nDigite um frase: ')).strip()
howmany = frase.upper().count('A')
find = frase.upper().find('A')+1
findlast = frase.upper().rfind('A')+1

print('A letra A aparece {} vezes'.format(howmany))
print('Primeira posição: {}'.format(find))
print('Última posição: {}'.format(findlast))
