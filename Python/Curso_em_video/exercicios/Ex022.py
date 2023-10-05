"""  
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
"""

nome = input('Informe seu nome: ')
primeiro_nome = nome.split()[0]

print(f'Nome em minusculo: {nome.lower()}')
print(f'Nome em maiusculo: {nome.upper()}')
print(f'Quantidade de letras: {len(nome.replace(" ", ""))}')
print(f'Quantidade de letras primeiro nome: {len(primeiro_nome)}')