""" Crie um programa onde o usuário possa digitar sete valores
numericos e cadastre-os em uma lista única que mantenha
separados os valores pares e impares. No final mostre os,
pares e impares em ordem crescente. """

lista_numeros = [[], [], []]

for i in range(7):
    lista_numeros[0].append(int(input('Informe um numero: ')))

# Analisando numeros dentro da lista composta para fazer a separação de pares e impares
for element in lista_numeros[0]:
    if element % 2 == 0:
        lista_numeros[1].append(element)
    elif element % 2 == 1:
        lista_numeros[2].append(element)

# Colocando lista em ordem crescente
lista_numeros[1].sort()
lista_numeros[2].sort()

print('-=' * 50)
print(f'Os numeros foram {lista_numeros[0]}', end='\n\n')
print(f'Pares foram, ', end='')
for i in lista_numeros[1]:
    print(f'{i}..', end='')
print(f'\nImpares foram, ', end='')
for i in lista_numeros[2]:
    print(f'{i}..', end='')
print('\n<<<<FIM>>>>')
