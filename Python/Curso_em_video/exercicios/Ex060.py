"""  
    Faça um programa que leia um número qualquer e mostre
    o seu fatorial.
    n! = n · (n-1) · (n-2) … 3 · 2 · 1
"""

# from math import factorial
fat = int(input('Informe o fatorial desejado: '))
result = fat
original_valuer = fat


print(f'Calculando {fat}! fatorial')
while fat > 0:
    if fat != 1:
        result *= fat - 1
        print(f'{fat} x', end=' ')
    fat -= 1

print(f'1 = {result}')




