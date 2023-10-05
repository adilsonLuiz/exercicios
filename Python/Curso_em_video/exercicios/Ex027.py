"""  
    Faça um programa que leia o nome completo de uma pessoa, 
    mostrando em seguida o primeiro e o último nome separadamente.
"""

nome = input('Informe seu nome completo: ').strip().title().split()

print(f'Seu primeiro nome {nome[0]}')
print(f'Seu ultimo nome {nome[-1]}')