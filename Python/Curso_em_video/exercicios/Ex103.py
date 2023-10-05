"""  
Faça um programa que tenha uma função chamada ficha(), que receba dois 
parâmetros opcionais: 
o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, 
mesmo que algum dado não tenha sido informado corretamente.
"""


def show_information_player(name_player='Augusto', gols=4):
    print('-' * 30)
    print(f'NOME: {name_player}')
    print(f'GOLS: {gols}')
    print('-' * 30)


name = str(input('Informe o nome do jogador: ')).strip().capitalize()
qtd_gols = int(input('Quantidade de gols realizados: '))
show_information_player(name, qtd_gols)
