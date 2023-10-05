"""  
 Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
 Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

def leia_int(txt):
    while True:
        try: 
            number = int(input(txt))
        except ValueError:
            print(f'\033[1;31mERRO! Informe apenas números inteiros\033[m')
        except KeyboardInterrupt:
            print('\nLeitura do numero cancelada pelo usuário')
            return 0
        else:
            return number


def leia_float(txt):
    while True:
        try:
            number= float(input(txt))
        except ValueError:
            print(f'\033[1;31mERRO! Informe penas números\033[m')
        except KeyboardInterrupt:
            print('\nLeitura do numero cancelada pelo usuário')
            return 0
        else:
            return number


number01 = leia_int('Informe um numero inteiro: ')
number02 = leia_float('Informe um numero Real: ')

print(f'N1: {number01}\nN2:{number02}')

