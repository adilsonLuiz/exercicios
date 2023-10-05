"""
Codifique um programa que leia um numero inteiro e mostre na tela o seu antercessor e
seu sucessor
"""
# 05/02/21 - Refazendo para adicionar cores de terminal

n1 = int(input('Informe um número inteiro: '))


print(f'Numero informado: \033[1;30m{n1}\033[m')
print(f'Antecessor: \033[31m{n1 - 1}\033[m') 
print(f'Sucessor: \033[34m{n1 + 1}\033[m') 


