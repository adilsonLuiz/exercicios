""" Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha. """



matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_terceira_coluna = 0
soma_valores_pares = 0

# Leitura de valores
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'informe um valor({linha})({coluna}): '))


print('\t\t\tMatriz digitada')
print('-=' * 50)
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

# Soma dos valores da terceira coluna
for linha in range(3):
    for coluna in range(3):
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]

# Soma de todos valores pares
for linha in range(3):
    for coluna in range(3):
        if matriz[linha][coluna]%2 == 0:
            soma_valores_pares += matriz[linha][coluna]

print(f'A soma de todos os valores pares foi de {soma_valores_pares}')
print(f'A soma da terceira coluna da matriz resultou em {soma_terceira_coluna}')
print(f'O maior valor da segunda linha foi {max(matriz[1])}')
