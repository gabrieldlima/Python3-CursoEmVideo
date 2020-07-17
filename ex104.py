# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só
# que fazendo a validação para aceitar apenas um valor numérico.


def readInt(msg):
    ok = False
    value = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            value = int(n)
            ok = True
        else:
            print('ERRO! Digite um número inteiro.')    
        if ok:
            break
    return value

n = readInt('Digite um número: ')
print(f'Você digitou o número {n}.')
