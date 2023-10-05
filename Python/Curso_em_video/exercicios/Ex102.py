"""  
Crie um programa que tenha uma função fatorial() 
que receba dois parâmetros: o primeiro que indique o número a calcular e 
outro chamado show, que será um valor lógico (opcional) indicando se será 
mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(number, show=True):
    from math import factorial

    result = number
    if show:
        print(f'Calculando {number}! fatorial')
        while number > 0:
            if number != 1:
                result *= number - 1
                print(f'{number} x', end=' ')
            number -= 1
        print(f'1 = {result}')
    else:
        result = factorial(number)
        print(f'O fatorial de {number} é {result}.')


fat = int(input('Informe o fatorial desejado: '))
option_show = str(input('Deseja mostrar informação na tela[S\\N]: ')).strip().upper()


if option_show == 'S':
    fatorial(fat)
else:
    fatorial(fat, False)
