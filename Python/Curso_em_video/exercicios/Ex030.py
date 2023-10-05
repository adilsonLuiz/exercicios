"""  
Crie um programa que 
    Entrada
        - leia um número inteiro
    Processamento
        - Descubra se ele é PAR ou ÍMPAR.
    Saida
        - Mostre na tela se ele é PAR ou ÍMPAR.
"""

number = int(input('Informe um numero inteiro: '))

if number%2 == 0:
    print(f'{number} é um número PAR: ')
else:
    print(f'{number} e um numero ÌMPAR')


