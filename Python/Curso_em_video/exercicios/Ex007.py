"""  
Codifique um programa que leia duas notas de um aluno, calcule e mostre a sua
"""
# 05/02/21 - Refazendo para adicionar cores de terminal

notas = list()

for n in range(2):
    notas.append(float(input('\033[1;33mInforme uma nota: \033[m')))


media = sum(notas) / 2

print(f'A media foi de \033[1;34m{media}\033[m')