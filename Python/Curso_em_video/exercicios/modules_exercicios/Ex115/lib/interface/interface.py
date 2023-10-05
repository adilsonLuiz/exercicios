
from lib.pessoa import pessoas

def print_line(line='-', size=30):
    return print(line * size)


def show_text_with_line(txt):
    print()
    print_line()
    print(f'{txt:^30}'.upper())
    print_line()
    print()


def color_in_text(txt, color_key):
    colors = {
        'red': '\033[1;31m',
        'yellow': '\033[1;33m',
        'green': '\033[1;32m',
        'blue': '\033[1;34m',
        'no_color': '\033[m',
    }

    return f'{colors[color_key]} {txt} {colors["no_color"]}'


def show_menu(options='', banner=''):
    cont = 1
    default_options = ['Ver pessoas Casdastradas',
                       'Cadastrar nova pessoa',
                       'Apagar dados',
                       'Sair do programa'
                       ]
    if not banner:
        show_text_with_line('menu principal')
    else:
        show_text_with_line(banner)
    if not options:
        for modulo in default_options:
            print(f'[{color_in_text(cont, "red")}] - {color_in_text(modulo, "yellow")}')
            cont += 1
    else:
        for modulo in options:
            print(f'[{color_in_text(cont, "red")}] - {color_in_text(modulo, "yellow")}')
            cont += 1


def execute_module01():
    pessoas.list_all_people()


def execute_module02():
    pessoas.set_new()


def execute_module03():
    close_program()


def close_program():
    show_text_with_line('Encerrando Programa')
    print(color_in_text('Obrigado por usar nosso sistema', 'green'))
    exit(0)


