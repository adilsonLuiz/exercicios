"""  
    Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""


digitos = int(input('Informe um numero de 0 a 9999: '))

print(f'O numero {digitos}, possui')



print(f'''
        {str(int(digitos / 1))[-1]} : Unidade
        {str(int(digitos / 10))[-1]} : Dezena
        {str(int(digitos / 100))[-1]} : Centena
        {int(digitos / 1000)} : Milhar
        ''')