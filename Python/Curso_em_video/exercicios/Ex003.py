# Codifique um programa que leia 2 números e exiba a soma entre eles.
# 05/02/21 - Refazendo para adicionar cores de terminal

""" # Método 1 - Utilizando list e functions

list_num = [int(input("Informe o Primeiro numero: ")), int(input("Informe o segundo número: "))]

print(f"{list_num[0]} + {list_num[1]} = {sum(list_num)}") """


# Método 2 - Modo Facil e simplificado

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))

print(f"A soma de \033[36m{n1}\033[m e \033[33m{n2}\033[m resultou em \033[1;34;40m{n1 + n2}\033[m")