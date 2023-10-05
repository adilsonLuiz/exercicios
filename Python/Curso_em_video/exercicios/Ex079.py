""" Crie um programa onde o usuario possa digitar varios valores numericos e, 
armazene-os em uma lista. Caso o numero ja exista la dentro,
ele nao sera adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente
 """

numeros = list()
while True:
    num = int(input('Informe um numero: '))
    while num in numeros:
        print(f'O numero {num}, ja existe, não adicionado !')
        num = int(input('Informe outro numero: '))
    
    numeros.append(num)
    print(f'Numero adicionado com sucesso !')
    resp = input('Continuar[S\\n]: ').strip().upper()[0]
    while resp not in 'NS ':
        resp = input('Continuar[S\\n]: ').strip().upper()[0]
    if resp == 'N':
        break

print(f'Sua lista original: {numeros}')
numeros.sort()
print(f'Lista ordenada: {numeros}')
