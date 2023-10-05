"""  
Faça um programa que 

Entrada
    - Leia um ano
Processamento
    - Calcular se ele é bissexto.
Saida
    - Mostre se ele é bissexto ou não.
"""
from datetime import date


year = int(input('Informe um ano: (Digite 0 para o ano atual) '))

if year == 0:
    year = int(date.today().year)
# Não consigo realizar o exercicio completo pois preciso de condições aninhadas (Ainda nao passado pelo curso)

if year%4 == 0 and year%100 != 0 or year%400 == 0:
    print(f'O ano {year} e um ano bissexto')
else:
    print(f'O ano {year} não é um ano bissexto')

