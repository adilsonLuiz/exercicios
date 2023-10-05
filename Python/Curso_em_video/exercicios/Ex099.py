"""
Codifique um programa que tenha uma função chamada maior(), que receba varios parametros como valores inteiros;
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(*num):

    cont = maior = 0

    print('Analisando números...')
    print('Numeros informados')
    for valores in num:
        print(f'{valores}', end=' ')
        if cont == 0:
            maior = valores
        elif maior < valores:
            maior = valores
        cont += 1
    print(f'\nO maior valor informado foi {maior}')


numbers= list()
debug = False

type_execution = int(input('Tipo de execução(0 - Debug, 1 - Normal): '))
if type_execution == 0:
    debug = True

while True:
    if not debug:
        numbers.append(int(input('Informe um numero: ')))
        resp = str(input('Deseja continuar? [S/n]: ')).strip().upper()[0]
        if resp == 'N':
            maior(numbers)
            del numbers
            print('<<<SAINDO>>>')
            break
    else:
        maior(2, 9, 4, 5, 7, 1)
        maior(4, 7, 0)
        maior(1, 2)
        maior()
        break







