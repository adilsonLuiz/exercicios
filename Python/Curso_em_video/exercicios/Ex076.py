"""  
Crie um programa que tenha uma tupla única com nomes de produtos 
e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, 
organizando os dados em forma tabular.
"""

products = (
            'lapis', 1.90,
            'borracha', 2,
            'apontador', 1.50,
            'notebook', 2500,
            'memoria RAM', 400,
            'caderno', 3.6,
            'mochila', 7.5,
            'Livros', 45.50
            )


print('-'* 40)
print('Lista de Preços'.center(40).upper())
print('-' * 40)



for index in range(0, len(products), 2):
    print(f'{products[index].capitalize():.<30}R$', end=' ')
    print(f'{products[index + 1]:>0.2f}')
print('-' * 40)