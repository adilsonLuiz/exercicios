"""  
 Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""

# Truncar o numero 


from math import trunc


number = float(input('Informe um número: '))

print(f'\033[1;31mA parte inteira do número informado é {trunc(number)}\033[m')