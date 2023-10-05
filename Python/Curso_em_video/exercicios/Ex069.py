"""  
    Crie um programa que 
    Leia idade e sexo de varias pessoas.
    O programa deverá ao final da leitura dos dados perguntar se o usuário quer continuar.

    Como saida
        Imprimir total de pessoas maior de 18 anos
        Impirmir total de homens
        Imprimir total de mulheres com menos de 20 anos.
"""


maior_idade = 0 
mulher_menor_idade = 0
total_homen = 0

print(f'-=' * 20)
print(f'\tCadastrar Pessoas')
print(f'-=' * 20)
while True:
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe seu sexo: ')).upper().strip()[0]

    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        total_homen += 1
    if sexo == 'F' and idade < 20:
        mulher_menor_idade += 1
    
    resp = str(input('Deseja continuar[S\\n]: ')).upper().strip()[0]
    if resp == 'N':
        break # Finaliza o looping
    
print(f'Total de pessoas com maior idade: {maior_idade}')
print(f'Total de homens: {total_homen}')
print(f'Total de mulheres com menos de 20 anos: {mulher_menor_idade}')


