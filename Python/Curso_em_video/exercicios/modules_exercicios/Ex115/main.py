"""
Vamos criar um interface em Python, usando modularização.
"""
from time import sleep

from lib.interface import interface
from lib.dados import dados
from lib.database import database


database.check_database_exist()
while True:
    try:
        interface.show_menu()
        modulo = dados.read_module()
        if modulo == 1:  # Ver pessoas cadastradas
            interface.execute_module01()
        elif modulo == 2:  # Cadastrar nova pessoa
            interface.execute_module02()
        elif modulo == 3:
            database.erase_database_data()
        elif modulo == 4:
            interface.close_program()
        else:
            print(interface.color_in_text(f'ERRO! Modulo {modulo} inexistente.', 'red'))
            sleep(1)
    except KeyboardInterrupt:
        interface.close_program()
