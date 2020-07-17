# DESAFIO 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas elei-
# ções.

def vote(year):
    from datetime import datetime
    
    current = datetime.today().year
    age = (current - year)

    if age < 16:
        return(f'Com {age} anos: NÃO VOTA.')

    elif 16 <= age < 18 or age > 65:
        return(f'Com {age} anos: VOTO OPCIONAL.')
        
    else:
        return(f'Com {age} anos: VOTO OBRIGATÓRIO')


yearBirth = int(input('Em que ano vocẽ nasceu: '))
print(vote(yearBirth))
