"""  
Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com
15% de aumento
"""

s = float(input('Informe seu salario: '))

n_saldo = s + s * 0.15

print(f'Seu novo salario com 15% de aumento ficara R${n_saldo}')