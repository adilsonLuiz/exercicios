"""  
Codifique um programa que leia o valor de um produto, e mostre o seu novo preço
com desconto de 5%
"""
# 05/02/21 - Refazendo para adicionar cores de terminal
produto = float(input('Informe o valor do produto: '))

n_price = produto - produto * 0.5

print(f'Este produto com \033[1;32m5%\033[m de desconto ficará \033[1;35mR${n_price}\033[m')