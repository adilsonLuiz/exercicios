from lib.database import database
from lib.interface import interface


def list_all_people():
    data = database.get_database_data()
    if not data:
        print(interface.color_in_text('Não há pessoas cadastradas', 'red'))
    else:
        pessoa_temp = str()
        interface.show_text_with_line('pessoas cadastradas')
        for pessoa in data:
            pessoa_temp = pessoa.split(';')
            print(f'{pessoa_temp[0]:<20}{pessoa_temp[1]:>20}')



def set_new():
    interface.show_text_with_line('cadastrar nova pessoa')
    name = str(input('Informe o nome e sobrenome: ')).strip().capitalize()
    idade = str(input('Informe a idade: '))
    data = f'{name}{";"}{idade}' + '\n'
    database.write_data(data)

