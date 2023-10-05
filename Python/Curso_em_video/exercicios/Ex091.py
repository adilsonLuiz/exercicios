"""
    Crie um programa onde 4 jogadores joguem um dado e tenham resultados
    aleatorios. 
    Guarde esses resultados em um dicionário. 

    No final coloque colocar esse dicinário em ordem, 
    sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
from time import sleep
from operator import itemgetter

players = dict()
MAX_DADO_VALUER = 6 # Representa um dado

for play in range(1, 5):
    number = randint(1, MAX_DADO_VALUER)
    players['player' + str(play)] = number
    print(f'{play}º jogandor tirou {number} no dado.')
    sleep(1)


print(f'{"Tabela de resultados":-^50}\n')

for index, winner in enumerate(sorted(
            players.items(), 
            key=itemgetter(1), 
            reverse=True)):
    print(f'{index + 1}º {winner[0]} tirou {winner[1]} no dado')
