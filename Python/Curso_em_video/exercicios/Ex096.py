"""
Faça um programa que tenha um função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) 
e mostre a área do terreno.
"""


def area(larg, compri):
    a = larg * compri
    print(f'Um terreno com {larg:.1f}x{compri:.1f} terá a área de {a}m²')


# Programa principal
l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l, c)
