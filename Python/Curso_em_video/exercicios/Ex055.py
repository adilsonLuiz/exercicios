"""
    Faça um programa que leia o peso de 5 pessoas.
    No final, mostre qual foi o maior e menor peso lidos.
"""


peso = list() 
for people in range(3):
    peso.append(float(input('Informe seu peso: ')))


print(f'O maior peso foi {max(peso)}')
print(f'O menor peso foi {min(peso)}')
