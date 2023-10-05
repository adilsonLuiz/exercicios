"""
Codifique um programa que tenha um lista chamada numeros e duas funções chamadas sorteia() 
e somaPar().
A primeira função vai sortear 5 numeros e vai coloca-las dentro da lista 
A segunda função vai mostrar a soma
entre todos os valores PARES sorteados pela função anterior
"""


def sort_num(list_numbers, rand_begin, rand_end):
    from random import randint
    number_radom = [randint(rand_begin, rand_end) for number in range(6)]
    for number in number_radom:
        list_numbers.append(number)


def sum_par(list_numbers):

    list_par = [number for number in list_numbers if number % 2 == 0]
    
    print('-' * 30)
    print('--- Valores sorteados ---')
    for number in list_numbers:
        print(f'{number}', end=' ')
    print()
    print('-' * 30)
    if not any(list_par):
        print('--- Não foi encontrado nenhum valor par ---')
        print('--- Não é possivel realizar a soma dos pares ---')
    else:
        print('--- Valores pares encontrados ---')
        for par in list_par:
            print(f'{par}', end=' ')
        print()
        print('-' * 30)
        print(f'A soma dos valores resultou {sum(list_par)}')


# Programa principal
from time import sleep
numbers_list = []
sort_num(numbers_list, 0, 100)
sum_par(numbers_list)

