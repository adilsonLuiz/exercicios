"""  
    Faça um programa que leia o sexo de uma pessoa
    mas so aceite os valores "M" ou "F".
    Caso esteja errado peça a entrada do dado até
    que o valor esteja correto
"""


sex = str(input('Informe seu sexo: ')).strip().upper()[0]

while sex not in ['M', 'F']:
    print('Valor não aceito, digite apenas "F" ou "M"')
    sex = str(input('Informe seu sexo: ')).strip().upper()[0]

print(f'Sexo {sex} registrado com sucesso.')