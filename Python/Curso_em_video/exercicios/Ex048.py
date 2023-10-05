"""
    Faça um programa que calcule a soma entre todos 
    os numeros impares que são multiplos de tres e
    que se encontram no intervalo de 1 até 500
"""

somatorio = 0

""" 
    for i in range(1, 501):
        if i%2 != 0: # Obtendo numeros impares
            if i % 3 == 0:
                somatorio += i # Calculando o multiplo de 3
    print(somatorio)
 """

"""  
    A complexidade do algoritmo acima também e pesada, podemos fazer o mesmo
    código com menos iterações
"""

somatorio = 0
total_num = 0

""" for i in range(1, 501, 2):
    if i % 3 == 0:
        total_num += 1
        somatorio += i """

#print(f'A soma dos {total_num} números resultou em {somatorio}')
 
# Utilizando metodo de list compreension
number = [ number for number in range(1, 501, 2) if number %3 == 0 ]
print(f'A soma dos {len(number)} resultou em {sum(number)}')