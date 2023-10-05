"""
Codifique um programa que leia um numero e mostre seu dobro, triplo e raiz quadrada
"""
# 05/02/21 - Refazendo para adicionar cores de terminal

numero = int(input('\033[1;31mInforme um número: \033[m'))

print(f'Número informado: {numero}')
print(f'Dobro: {numero * 2}')
print(f'Triplo: {numero * 3}')
print(f'Raiz Quadrada: {int(numero ** (1/2))}')