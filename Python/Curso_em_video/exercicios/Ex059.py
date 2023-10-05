"""  

  Crie um programa que leia dois valores e mostre um interface na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
    
    O programa deverá realizar a operação necessaria 
    para cada caso.
"""



# Global
finish_program = False
list_num = [ 0, 0 ]


def read_numbers():
    global list_num
    list_num[0] = int(input('Informe um número: '))
    list_num[1] = int(input('Informe outro número: '))


def print_main_menu() -> None:
    print(
        """
        O que você vai fazer agora?!

        [1] - Somar Números
        [2] - Multiplicar Números
        [3] - Imprimir maior Número
        [4] - Adicionar um novo Número
        [5] - Sair do Programa
        """
        )


def analise_choise(number: int):
    #Imports local

    from os import system

    global list_num
    global finish_program

    system('cls || clear')

    if number == 1: # Soma numeros
        print(f'A soma entre {list_num[0]} e {list_num[1]} lido resultou em {sum(list_num)}')
    elif number == 2: # Multiplicação dos numeros
        prod = list_num[0] * list_num[1]
        print(f'A multiplicação dos números {list_num[0]} e {list_num[1]} tem o seguinte produto {prod}')
    elif number == 3: # imprimir maior número
        if list_num[0] == list_num[1]:
            print('Não há valor maior, ambos são iguais')
        else:
            max_num = max(list_num)
            print(f'O maior número entre {list_num} é {max_num}')
    elif number == 4: # ler mais um número
        read_numbers()
    elif number == 5:
        print('Você escolheu sair do programa...')
        finish_program = True
    else:
        print('Opção invalida, digite novamente')
        
        
        


read_numbers()
while not finish_program:
    try:
        print_main_menu()
        option = int(input('Informe uma opção: '))
        analise_choise(option)
    except KeyboardInterrupt:
        print('\nPrograma interrompido')
        print('Saindo.')
        exit(1)

