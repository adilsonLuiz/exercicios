"""
Codificar um programa que leia uma informação pela stdin e 
informe o seu tipo primitivo, assim como todos os tipos de informações possiveis,
utilizando as funçoes bult in do Python """
# 05/02/21 - Refazendo para adicionar cores de terminal

from random import choices



thing = input('Digite algo: ')


print(f""" 

Conteudo digitado: \033[33m'{thing}'\033[m
Tipo de dado digitado: \033[1;31m {type(thing)} \033[m
Possui somente letras: \033[1;32m{thing.isalpha()} \033[m
Possui números e letras: \033[1;33m{thing.isalnum()}\033[m
Possui apenas digitos: \033[1;34m{thing.isdigit()}\033[m
Possui somente espaçoes: \033[1;35m {thing.isspace()} \033[m
Esta toda em minuscula: \033[1;30m{thing.islower()} \033[m
""")
