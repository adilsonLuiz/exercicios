"""
Codifique um programa que tenha uma função chamada contador(), 
que receba três parâmetros: inicio, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de 1 em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada
"""

from time import sleep

def contador(i, f, p):

    if p < 0:
        p = abs(p)
    if p == 0:
        p = 1
    
    if i > f: # Contagem regresiva 
        for cont in range(i, f - 1, -p):
            print(cont, end=' ')
            sleep(0.5)
        print('- Final da contagem')

    else:
        for cont in range(i, f + 1, p):
            print(cont, end=' ')
            sleep(0.5)
        print('- Final da contagem')
    print()






contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez, contagem personalizada')
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
contador(i, f, p)


     
