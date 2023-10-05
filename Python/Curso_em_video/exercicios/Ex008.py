"""  
Escreva um programa que leia um valor em metros e devolva em centimetros e milimetros
"""
# 05/02/21 - Refazendo para adicionar cores de terminal

from math import ceil

metros = float(input('\033[33mInforme os metros: \033[m'))

print(f'{ceil(metros)}m foi a medida informada')
print(f'{ceil(metros)}m -> {ceil(metros * 100)}cm')
print(f'{ceil(metros)}m -> {ceil(metros * 1000)}ml')