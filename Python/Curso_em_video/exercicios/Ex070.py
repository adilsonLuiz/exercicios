"""  
    Crie um programa que 
        Leia nome e preço de varios produtos.
        Verificar se deseja continuar a leitura
    Como saida
        Imprimir total de gasto na compra
        Quantos produtos custam mais de R$1000
        Qual o nome do produto mais barato
"""

from os import system



total_price = 0
expensive_price_prod = 0
name_nocive_prod = ''
frist_iteration = False
low_price = 0

while True:
    
    name_prod = str(input('Informe o nome do produto: '))
    price_prod = int(input('Informe o preço do produto: '))
    
    if not frist_iteration:
        low_price = price_prod
        name_nocive_prod = name_prod
        frist_iteration = True

    if price_prod > 1000:
        expensive_price_prod += 1

    if price_prod < low_price:
        low_price = price_prod
        name_nocive_prod = name_prod

    total_price += price_prod
    resp = str(input('Deseja continuar: [S\\n]: ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'------------- FIM DAS COMPRAS ----------------')
print(f'Total gasto na compra: \033[1;33m{total_price}\033[m')
print(f'Quantidade de produtos que custaram mais que R$1000: \033[1;32m{expensive_price_prod}\033[m')
print(f'O nome do produto mais barato é {name_nocive_prod}')