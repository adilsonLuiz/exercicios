""" Codifique um programa aonde o usuario possa digitar cinco valores numericos 
e armazene-os em uma lista, ja na posição corrente de inserção 
(sem usar o sort()). No final, mostre a lista ordenada na tela """

numeros = list()

for cont in range(5):
    n = int(input('Informe um numero: '))
    if cont == 0 or n > numeros[-1]:
        numeros.append(n)
    else:
        index = 0
        while index < len(numeros):
            if n <= numeros[index]:
                numeros.insert(index, n)
                break
            index += 1
    
print(numeros)
    










