"""  
Crie um programa que tenha uma função chamada voto() 
que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, 
OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def analisa_voto(ano_nascimento):
    from datetime import date

    idade = date.today().year - ano_nascimento

    if idade < 18:
        return 'NEGADO'
    elif 18 <= idade < 65:
        return 'OBRIGATORIO'
    return 'OPCIONAL'


data_nascimento = int(input('Informe a data de nascimento: '))
print(f'Status para voto: {analisa_voto(data_nascimento)}')
