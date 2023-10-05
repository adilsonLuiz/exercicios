"""
    Desenvolva um programa que leia o nome, idade e sexo
    de 4 pessoas. No final moste.

    > A media de idade do grupo
    > Qual é o nome do homen mais velho
    > Quantas mulheres tem menos de 20 anos.
"""

name = ''
age = ''
sex = ''

data_process = {
                'average_age': 0, 
                'old_man_name': '',
                'woman_age': 0,
                'old_man_age': 0,
                'ages': 0,
                }

# Entrada
for index, p in enumerate(range(0, 4)):
    print(f'======= Pessoa {index + 1} ========')
    name = str(input('Nome: ')).lower()
    age = int(input('Idade: '))
    sex = str(input('Sexo: ')).lower()
    if p == 0 and sex in 'm':
        data_process['old_man_name'] = name
        data_process['old_man_age'] = age
    if sex == 'm' and age > data_process['old_man_age']:
        data_process['old_man_name'] = name
        data_process['old_man_age'] = age

    if sex in 'f' and age < 20: # Se isso for verdadeiro o contador de mulheres ira ser incrementado
        data_process['woman_age'] += 1

    data_process['ages'] += age
    
# Calculado media da idade
data_process['average_age'] = data_process['ages'] / 4


# Saida de dados

print(f'A média de idade do grupo é de {data_process["average_age"]} anos')
print(f'O homen mais velho tem {data_process["old_man_age"]} anos e se chama {data_process["old_man_name"]}.')
print(f'Ao todo são {data_process["woman_age"]} mulheres com menos de 20 anos')