""" Faça um programa que faça o computador jogar 
Jokenpô com você"""


from random import randint


itens = ('pedra', 'papel', 'tesoura')


computer = randint(0, 2)

print(""" 
    Escolha sua opção
    [0] - Pedra
    [1] - Papel 
    [2] - Tesoura
""")

player = int(input('Escolha: '))

print('-=' * 20)
print(f'O computador escolheu {itens[computer]}')
print(f'O jogador escolheu {itens[player]}')
print('-=' * 20)


if computer == 0: # PEDRA
    if player == 0:
        print('Esta jogada resultou em um empate!')
    elif player == 1:
        print('Parabêns você venceu!')
    elif player == 2:
        print('Esta não! O computador venceu você!')

elif computer == 1: # PAPEL
    if player == 0:
        print('Esta não! O computador venceu você!')
    elif player == 1:
        print('Esta jogada resultou em um empate!')
    elif player == 2:
        print('Parabêns você venceu!')

elif computer == 2: # TESOURA
    if player == 0:
        print('Parabêns você venceu!')
    elif player == 1:
        print('Essa não! O computador venceu você!')
    elif player == 2:
        print('Esta jogada resultou em um empate!')