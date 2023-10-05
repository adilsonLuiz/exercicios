"""  
Desenvolva um programa que
Entrada
    - leia o comprimento de três retas
    
Processamento
    - Calcular e verificar se as retas podem forma um triangulo

Saida
    - Exibir informações obtidas
"""

reta1 = float(input('Informe o primeiro seguimento: '))
reta2 = float(input('Informe o segundo seguimento: '))
reta3 = float(input('Informe o terceiro seguimento: '))


if reta1 < reta2 + reta3 and reta1 > abs(reta2 - reta3):
    print('Com essas medidas podemos fazer um triangulo')
else:
    print('Com essas medidas não podemos fazer um triangulo')
