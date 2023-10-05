"""  
    Crie um programa que 
    - leia varios numeros inteiros
    - imprima a media entre eles
    - imprima o maior valor lido
    - imprima o menor valor lido
    - criar condição para parada do programa
"""
from math import ceil



media = 0
soma_valores = 0
cont_num = 0

num = int(input('Informeu um número: '))
maior = menor = num
while num != -999:
    if num != -999:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
        cont_num += 1
        soma_valores += num
        num = int(input('Informeu um número: '))
    
media =  ceil(soma_valores / cont_num)
print(f'O maior valor lido foi {maior}')
print(f'O menor valor lido foi {menor}')
print(f'A media deles foi de {media}')