# Escreva um programa que leia o nome do usuário e imprima uma mensagem de boas vindas.
# 05/02/21 - Refazendo para adicionar cores de terminal

nome = input("Informe seu nome: ")
print(f"Seja bem vindo, \033[4;31m{nome} \033[m\n")
