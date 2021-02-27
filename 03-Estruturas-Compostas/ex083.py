# DESAFIO 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
# analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = str(input('Digite um expressão numérica: ')).strip()
stack = list()
for item in expression:
    if item == '(':
        stack.append('(')
    elif item == ')':
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(')')
            break

if len(stack) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
