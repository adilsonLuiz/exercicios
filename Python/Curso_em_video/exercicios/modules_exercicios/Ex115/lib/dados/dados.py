from lib.interface import interface


def leia_int(txt):
    while True:
        try: 
            number = int(input(txt))
        except ValueError:
            print(f'\033[1;31mERRO! Informe apenas números inteiros\033[m')
        except KeyboardInterrupt:
            print('\nLeitura do numero cancelada pelo usuário')
            return 4
        else:
            return number


def read_module():
    module = leia_int(interface.color_in_text('Informe um modulo: ', 'blue'))
    return module


    

