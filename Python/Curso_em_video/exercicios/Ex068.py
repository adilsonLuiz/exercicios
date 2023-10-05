"""  
    Criar um programa que jogue par ou impar com o computador.
    O programa so deverá parar quando o jogador perder.
    Como saida o programa deverá exibir o total de vitorias consecutivas que o jogador conquistou.

    Havia feito esta solução com uma flag de controle, porém, como o intuito dos exercicios e fixar o looping infinito, junto com o break,
    decidi mudar a solução
"""

from random import choice



total_winner_count = 0
while True:
    computer_number = choice(range(10))
    player_number = int(input('Informe um número: '))
    player_choise = int(input('Ímpar[0] ou Par[1]: '))
    # Verificando se jogador quer par ou impar
    if player_choise == 0:
        computer_choise = 1
    else:
        computer_choise = 0
    sum_match = computer_number + player_number # Somando resultado
    
    if sum_match%2 == 0 and player_choise == 1: #
        total_winner_count += 1
        print(f'Parabéns, voce ganhou esta rodada o resultado e Par')
        print(f'Você jogou {player_number}, computador jogou {computer_number}')
    elif sum_match%2 > 0 and player_choise == 0:
        print(f'Parabéns, voce ganhou esta rodada o resultado e Impar')
        print(f'Você jogou {player_number}, computador jogou {computer_number}')
    else:
        print(f'Você perdeu!!')
        print(f'Você jogou {player_number}, computador jogou {computer_number}')
        print(f'Total de vitorias consecutivas {total_winner_count}')
        break
