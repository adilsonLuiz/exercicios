""" Faça um programa que ajude um jogador da MEGA SENA
a criar palpites. O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre
1 e 60 para cada jogo, cadastrando tudo em uma lista
composta """

from random import randint
from time import sleep

# Variaveis globais
lista_main_jogos = []
num_jogos = 0


print(f'============== MEGA SENA DA VIRADA =====================')
num_jogos = int(input('Digite quantos jogos deseja criar: '))

# Criando um lista dentro da lista main para cada jogo
for i in range(num_jogos):
    lista_main_jogos.append(list())

for indice_atual in range(len(lista_main_jogos)):
    jogo_sortido = list()
    for indice_sort in range(6):
        sort_num = randint(0, 60)
# Logica criada para nao deixar elementos se reperitem dentro dos jogos
        while sort_num in jogo_sortido:
            sort_num = randint(0, 60)
        lista_main_jogos[indice_atual].append(sort_num)
    # Apagando lista com numeros sortidos, para um nova criação
    jogo_sortido.clear()
    lista_main_jogos[indice_atual].sort()

# Exibindo jogos
print('=-' * 50)
for i, v in enumerate(lista_main_jogos):
    print(f'\tJogo [{i+1}] - {v}')
    sleep(1)
print('\n\tBoa sorte !')
