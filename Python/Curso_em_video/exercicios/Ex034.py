"""  
Escreva um programa que 
Entradas
    - pergunte o salário de um funcionário e 
Processamento
    - calcule o valor do seu aumento.
    OBS:
        salários > R$1250,00 : Juros de 10%
        salários <= R$1250,00: Juros de 15%
Saida
    - Imprima o novo salario 
"""

old_sal = float(input('Qual o seu salario atual: '))

if old_sal > 1250:
    new_sal = old_sal + float((old_sal * 0.10))
else:
    new_sal = old_sal + float((old_sal * 0.15))

print(f'Seu novo salario sera de R${new_sal}')