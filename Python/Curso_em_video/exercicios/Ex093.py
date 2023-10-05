"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou . Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante 
o campeonato.
"""

jogador = dict()
jogador['total_gol_campeonato'] = 0

jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas_jogadas'] = int(input('Partidas jogadas: '))
jogador['gol_partida'] = list()

for gol in range(jogador['partidas_jogadas']):
    jogador['gol_partida'].append(
        int(input(f'Gols feitos na {gol + 1}º partida: '))
        )
    jogador['total_gol_campeonato'] += jogador['gol_partida'][gol]

print(jogador)
print(f'''
    Nome do jogador: {jogador["nome"]}
    Total de Gols: {jogador["total_gol_campeonato"]}
    Patidas jogadas: {jogador["partidas_jogadas"]}
    '''
    )

print('Resultado de cada partida')
for partida in range(jogador['partidas_jogadas']):
    print(f'''
    {partida + 1}º Partida 
    {jogador["gol_partida"][partida]} Gols realizados
    '''
    )
