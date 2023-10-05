"""  
Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. 
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. 
Importante: use cores.
"""

cores = ('\033[m',  # Sem cor
         '\033[1;31m',  # Vermelho
         '\033[1;33m',  # Amarelo
         '\033[1;36m',
         '\033[1;30m',  # Branco
         )


def help_function(module):
    print(cores[4])
    help(module)
    print(cores[0])


def show_title(msg, cor):
    size_msg = len(msg)

    print(cores[cor])
    print('~' * size_msg)
    print(msg)
    print('~' * size_msg)
    print(cores[0])


while True:
    show_title('Sistema de ajuda para comandos', 1)
    print(cores[2])
    word = str(input('Informe um comando ou biblioteca => ')).strip().lower()
    print(cores[0])
    if word == 'fim':
        break
    help_function(word)
print('Volte novamente, fim do programa.')
