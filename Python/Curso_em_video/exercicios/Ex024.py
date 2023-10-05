"""  
    Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""

cidade = input('Informe o nome da cidade: ')

cidade = cidade.strip().upper().split()

print('SANTO' in cidade[0])