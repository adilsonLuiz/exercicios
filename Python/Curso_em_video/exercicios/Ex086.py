"""  Crie um programa que crie um matriz de dimensão 3x3
 e preencha com valores lidos pelo teclado.
 Ex:
   [][][]
   [][][]
   [][][]

No final, mostre a matriz na tela, com a formatação correta """

matriz = [[], [], []]




# Leitura de valores
for i in range(3):
    print(f'Posição [0][{i}]: ', end='')
    matriz[0].append(input())
for i in range(3):
   print(f'Posição [1][{i}]: ', end='')
   matriz[1].append(input())
for i in range(3):
    print(f'Posição [2][{i}]: ', end='')
    matriz[2].append(input())


print('-=' * 50)
print('\tMatriz 3x3\n')

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

