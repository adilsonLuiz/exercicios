"""  
 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
 Depois disso, mostre a listagem de números gerados e 
 também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

RANDOM_LIMIT_VALUER = 100

# Não vou utilizar lista, pois o desafio e resolver o problema com os recursos passados até então.
random_numbers = (
                    randint(0, RANDOM_LIMIT_VALUER),
                    randint(0, RANDOM_LIMIT_VALUER),
                    randint(0, RANDOM_LIMIT_VALUER),
                    randint(0, RANDOM_LIMIT_VALUER),
                    randint(0, RANDOM_LIMIT_VALUER),
                )

print(f'Tupla com valores gerados: ', end=' ')
for number in random_numbers:
    print(number, end=' ')
print(f'\nO maior valor é {max(random_numbers)}')
print(f'O menor valor é {min(random_numbers)}')