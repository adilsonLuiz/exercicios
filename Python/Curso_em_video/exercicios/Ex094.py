"""
Crie um programa que leia nome, sexo e idade de varias pessoas,
guardando os dados de cada pessoa em um dicionário em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo.
c) Uma lista com todas as mulheres.
d) Uma lista com todas as pessoas com idade acima da media
"""

from math import trunc

pessoas_cadastradas =  []
dados_processados = {
                    'pessoas_cadastradas': 0,
                    'media_idade': 0,
                    'mulheres': [],
                    'acima_idade': [],
                    }
cadastro_atual = 0

while True:
    pessoas_cadastradas.append(dict())
    pessoas_cadastradas[cadastro_atual]['nome'] = str(input('Nome: '))
    while True: # Otima forma de validar um dado
        pessoas_cadastradas[cadastro_atual]['sexo'] = \
            str(input('Sexo: ')).upper()[0]
        if pessoas_cadastradas[cadastro_atual]['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F', end=' ')

    pessoas_cadastradas[cadastro_atual]['idade'] = int(input('Idade: '))
    dados_processados['pessoas_cadastradas'] += 1
    while True: # Validando dado
        continuar = str(input('Continuar: S ou N: ')).upper()[0]
        if continuar  in 'NS':
            break
        print('ERRO! digite apenas S ou N')
    if continuar == 'N':
        dados_processados['media_idade'] /= cadastro_atual
        break
    dados_processados['media_idade'] += \
        pessoas_cadastradas[cadastro_atual]['idade']
    cadastro_atual += 1

for pessoa in pessoas_cadastradas:
    for key, valuer in pessoa.items():
        if key == 'sexo' and valuer == 'F':
            dados_processados['mulheres'].append(pessoa['nome'])
        elif key == 'idade' and valuer >= trunc(dados_processados['media_idade']):
            dados_processados['acima_idade'].append(pessoa['nome'])
print('=' * 30)
print(f'''
Pessoas cadastradas: {dados_processados["pessoas_cadastradas"]}
A media de idade: {trunc(dados_processados["media_idade"])}''')
print(f'As mulheres cadastradas', end=' ')
for pessoa in dados_processados['mulheres']:
    print(pessoa, end=' ')
print()
print('Pessoas acima da idade media:', end=' ')
for pessoa in dados_processados['acima_idade']:
    print(pessoa, end=',')

