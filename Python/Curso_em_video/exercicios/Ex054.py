""" 
    Crie um programa que leia o ano de nascimento de 
    sete pessoas. No final, mostre quantas pessoas ainda
    não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

year = int(date.today().year)
max_age = min_age = 0


for index, people in enumerate(range(1, 8)):
    date_birthday = int(input(f'Informe seu ano de nascimento ({index + 1}): '))
    age = year - date_birthday # Calculando e atribuindo idade da pessoa.
    if age < 18:
        min_age += 1
    else:
        max_age += 1

print(f'{max_age} pessoas possuem a maioridade')
print(f'{min_age} pessoas possuem a menoridade')