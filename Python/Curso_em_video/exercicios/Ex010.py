"""  
Faça um programa que leia quanto de dinheiro a pessoa tem na carteira e mostre 
quantos dolares ela pode comprar

Considerar dolar US: R$= 3,27
"""
# 05/02/21 - Refazendo para adicionar cores de terminal


DOLLAR = 0.18
r = float(input('\033[1;33mInforme quantos Reais você possui: \033[m'))

tot_dollar = r * DOLLAR

print(f'Com R${r} você consegue comprar U${tot_dollar}')
