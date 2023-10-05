"""
    Faça um programa que leia um numero inteiro e
    diga se ele é ou não um número primo
"""

num = int(input('Informe um numero: '))
cont = 0 # Contabilizar numeros divisiveis

# Minha solução
""" if num%1 == 0 and num%num == 0: # Formula para verificar se o numero e primo.
    print('Numero primo') """

# A forma acima esta errada, pois não conseguimos verificar se um número e realmente primo sem dividir ele por um intervalo


# Solução proposta pelo guanabara.

for i in range(1, num + 1):
    
    # Esquema de cores no terminal, para demostrar se o numero e divisivel ou não
    if num % i == 0:
        print('\033[33m', end=' ') # Cor amarela
        cont += 1 # Contabiliza total de números pares
    else:
        print('\033[31m', end=' ') # Cor vermelha
    print(f'{i}', end=' ')
print(f'\nO numero {i} foi divisivel {cont} vezes')

if cont <= 2:
    print(f'O número {num} é PRIMO e foi divisivel por {cont} números.')
else:
    print(f'O número {num} NÂO É primo!')