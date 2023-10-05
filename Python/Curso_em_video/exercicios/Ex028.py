"""  
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
 
 Processamento
 - Usuário tentar descobrir qual foi o número escolhido pelo computador.
 
 Saida
 - O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""

from random import randint

computer_choise = randint(0, 5)
user_coise = int(input('Informe um número de 0 - 5: '))

if user_coise == computer_choise:
    print(f'Usuario: {user_coise} x Computador: {computer_choise}, voce ganhou')
else:
    print(f'Usuário: {user_coise} x Computador: {computer_choise}, voce perdeu')