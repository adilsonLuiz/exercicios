# Codifique um programa que leia o nome e o peso
# de varias pessoas, guarde tudo em uma lista.
# No final, mostre: 
#
# A) Quantas pessoas foram cadastradas
# B) Uma lista com as pessoas mais pesadas
# C) Uma listagem com as pessoas leves 


pessoas_cadastras = list()
cadastro_atual = 0
maior_peso = menor_peso = 0



while True:
    pessoas_cadastras.append(list())
    pessoas_cadastras[cadastro_atual].append(str(input('Nome: ')))
    pessoas_cadastras[cadastro_atual].append(float(input('Peso: ')))
    if cadastro_atual == 0:
        maior_peso = menor_peso = pessoas_cadastras[cadastro_atual][1]
    else:
        if pessoas_cadastras[cadastro_atual][1] > maior_peso:
            maior_peso = pessoas_cadastras[cadastro_atual][1]
        elif pessoas_cadastras[cadastro_atual][1] < menor_peso:
            menor_peso = pessoas_cadastras[cadastro_atual][1]
        
    continuar = str(input('Continuar[S\\N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
    cadastro_atual += 1

print(f'Ao total foram cadastradas {len(pessoas_cadastras)} pessoas.')
print(f'Maior peso foi de {maior_peso}Kg, peso de ', end='')
for pessoa in pessoas_cadastras:
    if pessoa[1] == maior_peso:
        print(f'...{pessoa[0]}', end=' ')
print('\n')
print(f'Menor peso foi de {menor_peso}Kg, peso de ', end='')
for pessoa in pessoas_cadastras:
    if pessoa[1] == menor_peso:
        print(f'...{pessoa[0]}', end=' ')