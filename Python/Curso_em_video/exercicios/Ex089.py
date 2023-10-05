""" Crie um programa que leia nome e duas notas de 
varios alunos e guarde tudo em uma lista composta
No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas
de cada aluno individualmente

Guia de indice para lista composta:

lista_main_escola, criada para armazenar todos os dados recebidos do programa,
e armazenalos,
em listas 
lista_main_escola[0] -  Lista principal aonde fica todas sublistas
lista_main_escola[0][0] - Lista com nome dos alunos registados
lista_main_escola[0][1] - Lista com as notas, gravadas em listas cada 
um com 2 objetos 
lista_main_escola[0][2] - Lista com todas as medias de notas dos alunos  """

# Variaveis globais
lista_main_escola = [[[], [], []]]
indice_notas = 0
# FINALIZADO
while True:
# Lendo nome do aluno
    lista_main_escola[0][0].append(input('Nome: '))
    # Adicionando uma lista previa para armazenamento da notas
    lista_main_escola[0][1].append(list()) 
# Ler notas do aluno atual 
    for i in range(2):
        print(f'Nota {i+1}: ', end='')
        lista_main_escola[0][1][indice_notas].append(float(input()))

# Validar continuação
    resp = str(input('deseja continuar[S//N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    indice_notas += 1

# Calculando medias de todos os alunos FINALIZADO
for calc_med in range(len(lista_main_escola[0][1])):
    lista_main_escola[0][2].append( \
    float(sum(lista_main_escola[0][1][calc_med]) / 2))


# Imprimindo nome aluno e medias - FINALIZADO

print(f'{"BOLETIM":-^42}\n')
print(f'{"ID":<0} {"=" * 13} {"NOME":^5} {"=" * 13} {"MEDIA":>2}\n')
for index in range(len(lista_main_escola[0][0])):
    print(f'{index:<0}', end='') 
    print(f'{lista_main_escola[0][0][index]:-^35}', end='')
    print(f'{round(lista_main_escola[0][2][index], 1):>2}')
print('\n\n')

# Disponibilizando a consulta de notas para o usuario

while True:
    temp_consul = int(input('Qual aluno deseja consultar(-97 interrompe): '))
    if temp_consul == -97:
        print('<<<<< EXERCICO COMPLETADO COM SUCESSO >>>>>')
        print(lista_main_escola)
        break


    # Exibindo o nome do aluno
    print('-=' * 50)
    print(f'{lista_main_escola[0][0][temp_consul]} tirou as notas - '\
            f'{lista_main_escola[0][1][temp_consul]}')


