"""  
Faça um programa que leia um numero qualquer e mostre na tela a sua tabuada.
"""
# 05/02/21 - Refazendo para adicionar cores de terminal


def printTab(num: int) -> None:

    for tab in range(0, 11):
        print(f'\033[1;33m{num}\033[m x \033[1;34m{tab}\033[m = \033[1;032m{num * tab}\033[m')


tabuada_num = int(input('Informe um numero: '))

printTab(tabuada_num)