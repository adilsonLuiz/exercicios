# Codifique um programa que vai ler varios numeros e colocar em um lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# impares digitados, respectivamente.
# Ao final, moste o conteúdo das três listas geradas

main_list = list()
par_list = list()
impar_list = list()

# Inicio do codigo
while True:
    number = int(input('Informe um numero inteiro qualquer: '))

    if number%2 == 0:
        par_list.append(number)
    else:
        impar_list.append(number)
    main_list.append(number)
    resp = input('Deseja continuar[S/n]: ')
    if resp in 'Nn':
        break

print(f'A lista principal fornecida foi {main_list}')
print(f'Uma lista com valores PARES foi gerada, com os valores {par_list}')
print(f'Outra lista com valores IMPARES também foi gerada, com os valores {impar_list}')
