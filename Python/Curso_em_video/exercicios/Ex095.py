"""
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento
de cada jogador.
"""
time = list()
jogador = dict()

while True:
    jogador['nome'] = str(input('Nome: '))
    jogador['total_gol_campeonato'] = 0
    jogador['partidas_jogadas'] = int(input(f'Partidas jogadas por {jogador["nome"]}: '))
    jogador['gol_partida'] = list()

    for gol in range(jogador['partidas_jogadas']):
        jogador['gol_partida'].append(
            int(input(f'\tGols feitos na {gol + 1}º partida: '))
        )
        jogador['total_gol_campeonato'] += jogador['gol_partida'][gol]

    time.append(jogador.copy())
    jogador.clear()
    while True:
        continuar = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if continuar == 'N':
        break

print('Consultar jogador em especifico')
while True:
    print('-' * 35)
    print('Digite o número do jogador para realizar a consulta(-97 sair).\n')
    for index, jogador in enumerate(time):
        print(f'Jogador [{index + 1}] --> {jogador["nome"].capitalize()}')
    print('-' * 35)
    while True:
        consulta = int(input('Informe o numero do jogador: '))
        if consulta == -97:
            break
        elif consulta <= len(jogador):
            break
        print('ERRO! Valor não disponivel, tente novamente.')
    if consulta == -97:
        break
    print('-=' * 30)
    print(f'Levantamento do jogador {time[consulta - 1]["nome"].capitalize()}')
    for key, valuer in time[consulta - 1].items():
        if key == 'nome':
            continue
        elif key == 'gol_partida':
            for index, gol in enumerate(valuer):
                print(f'\t\t{index + 1}º Partida: {gol} Gols')
            continue
        print(f'\t{key.replace("_", " ").capitalize()}: {valuer}')
    print('-=' * 30)
print('<<<<Fim do programa>>>>>')
