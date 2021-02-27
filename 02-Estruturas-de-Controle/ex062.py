# DESAFIO 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa en-
# cerrará quando ele disser que quer mostrar 0 termos.

print('====== GERADOR DE PROGRESSÃO ARITIMÉTICA ======')

a1 = int(input('Primeiro termo: '))
reason = int(input('Razão: '))
term = a1
count = 1
total = 0
more = 10

while more != 0:
    total = total + more
    while count <= total:
        print('{} - '.format(term), end=' ')
        term += reason
        count += 1
    print('PAUSA')
    more = int(input('Quantos termos você quer ver a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')
