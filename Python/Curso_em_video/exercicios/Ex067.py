"""  
    Criar um programa que leia um numero e imprima uma tabuada do numero lido respectivamente.
    O programa deverá parar quando o número lido for negativo.
"""
from os import system

def print_tab(num: int) -> None:
    system('cls')
    limit = 0

    while limit < 11:
        print(f'{num} x {limit} = {num * limit}')
        limit += 1




while True:
    number_tab = int(input('Informe um número para exibir a tabuada: '))

    if number_tab < 0:
        break
    print_tab(number_tab)

print('Fim do programa')