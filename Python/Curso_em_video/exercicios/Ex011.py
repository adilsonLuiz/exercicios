"""  
Faça um programa que leia a largura e altura de uma parede em metros.
Calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo que
cada litro de tinta penta uma area de  2m²
"""
# 05/02/21 - Refazendo para adicionar cores de terminal
from math import ceil

largura = float(input('\033[1;35mInforme a largura da parede: \033[m'))
altura = float(input('\033[1;34mInforme a altura da parede: \033[m'))

a =  largura * altura 

print(f'Uma parede de {ceil(largura)}x{ceil(altura)}, tem uma area de {ceil(a)}')

litro_tinta = 2 * a

print(f'Tinta gasta para pintar parede: {ceil(litro_tinta)} litros')