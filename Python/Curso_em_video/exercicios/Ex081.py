# Crie um programa que vai ler varios numeros e colocar em uma lista. 
# Depois disso, mostre:
# A) quantos numeros foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e esta ou nao na lista

num_list = list()


while True:
    num_list.append(int(input('Informe um numero inteiro: ')))
    resp = input('Deseja continuar[S/n]: ').strip().upper()[0]
    if resp == 'N':
        break

num_list.sort(reverse=True)
print(f'Quantidade de numeros digitados {len(num_list)}')
print(f'A lista digitada em ordem inversa  {num_list}')
if 5 in num_list:
    print(f'O numero 5 foi digitado, e se encontra na posição {num_list.index(5)}')
else:
    print('O numero 5 não foi digitado nessa lista.')
    

