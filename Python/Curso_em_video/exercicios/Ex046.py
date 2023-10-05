""" 
    Faça um programa que mostre na tela uma contagem
    regressiva, de 10 até 0, com pausa de 1 segundo 
    entre eles.
"""


from time import sleep


print('Contagem iniciada para lançamento de fogos.')
for i in range(10, -1, -1): # Realizando o laço for para repetir a cotagem decrementando uma unidade 
    print(i)
    sleep(1) # Função Sleep para dar o tempo de 1 segundo solicitado.
print('BOOOW')