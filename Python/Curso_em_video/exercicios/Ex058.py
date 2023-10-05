"""  
   

Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” 
em um número entre 0 e 10. Só que agora o jogador vai tentar 
adivinhar até acertar, mostrando no final quantos palpites foram 
necessários para vencer.


"""

from random import randint


player_win = False
trying = 0
computer_choise = randint(0, 10)
while not player_win:
    
    user_coise = int(input('Informe um número de 0 - 10: '))

    if user_coise == computer_choise:
        print(f'\nSua jogada: [{user_coise}]\nJogada do Computador: [{computer_choise}]\nVoce ganhou!!!')
        print(f'Total de tentativas usadas {trying}')
        player_win = True
    else:
        if user_coise < computer_choise:
            print('Voce chutou baixo .. tente um numero maior...')
        else:
            print('Voce chutou alto ... tente um numero menor...')
        trying += 1
    

