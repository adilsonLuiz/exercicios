# Codifique um programa que leia 5 valores numericos e guarde-os em uma lista
# no final, mostre qual foi o maior e o menor valor digitado e as suas 
# respectivas posições na lista


num_list = list()



for cont in range(0, 5):
    num_list.append(int(input('Informe um numero: ')))

maior = max(num_list)
menor = min(num_list)

print(f'A lista digitada foi {num_list}')
print(f'O maior valor foi {maior}, nas posições ', end='')

# Logica para pegar os index do maior valor
for index, number in enumerate(num_list):
    if number == maior:
        print(f'{index}...', end='')

# Logica para pegar os index do menor valor
print(f'\nO menor valor foi {menor}, nas posições ', end='')
for index, number in enumerate(num_list):
    if number == menor:
        print(f'{index}...', end='')
