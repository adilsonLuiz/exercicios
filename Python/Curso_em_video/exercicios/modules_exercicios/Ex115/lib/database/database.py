import os

hostname = os.getlogin()
files_in_dbpath = os.listdir()

db_name = 'Pessoas_Cadastradas.txt' # database name file


def check_database_exist():
    if db_name not in files_in_dbpath:
        open(db_name, 'wt+')  # Criando arquivo
    else:
        print('Arquivo de dados já existe')


def close_connection(database):
    database.close()


def open_database_to_read():
    return open(db_name, 'r')


def open_database_to_write():
    return open(db_name, 'w')


def erase_database_data():
    db = open_database_to_write()
    db.writelines('')
    close_connection(db)


def get_database_data():
    file = open_database_to_read()
    return file.readlines()  # Removendo espaços excedentes


def write_data(new_data):
    file = open(db_name, 'at')
    file.write(new_data)
    close_connection(file)






