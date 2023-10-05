"""  
    Crie um programa que simule um caixa eletronico
        Leia o valor a ser retirado
    
    Como saida
        O programa vai infromar quantas cédulas de cada valor será entregue
    Obs:
        Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""
from os import system

# Variaveis globais utilizadas no programa
cedula_50 = 50
cedula_20 = 20
cedula_10 = 10
cedula_1 = 1

# Contador para cedulas usadas durante o processo de saque
total_cedula_50 = 0
total_cedula_20 = 0
total_cedula_10 = 0
total_cedula_1 = 0

saque_contabilizado = 0 # Ira contabilizar o valor do saque total escolhido pelo usuário.

system('cls || clear')
print('-=-=-=-=-=-=- BANCO AD SOLUTION -=-=-=-=-=-=-')
saque_selecionado = int(input('Informe o valor do saque: '))
saque_restante = saque_selecionado # Ira contabilizar o total de saque que ainda falta ser realizado

while True:
    if saque_restante%cedula_50 == 0:
        total_cedula_50 += 1 # Contabilizo total de cedula usada
        saque_contabilizado += cedula_50 # Somo o valor da cedula ao total do saque
        saque_restante -= cedula_50
    elif saque_restante%cedula_20 == 0:
        saque_contabilizado += cedula_20
        total_cedula_20 += 1
        saque_restante -= cedula_20
    elif saque_restante%cedula_10 == 0:
        saque_contabilizado += cedula_10
        total_cedula_10 += 1
        saque_restante -= cedula_10
    else:
        saque_contabilizado += cedula_1
        total_cedula_1 += 1
        saque_restante -= cedula_1
    
    # Condição de parada
    if saque_contabilizado == saque_selecionado:
        break


system('cls || clear')
print(f'*-' * 50)
print(f'Valor do saque realizado {saque_contabilizado}')
print(f"""
    Tota cedulas de 50: {total_cedula_50}
    Total cedulas de 20: {total_cedula_20}
    Total cedulas de 10: {total_cedula_10}
    Total cedulas de 1: {total_cedula_1}
    """)
print(f'*-' * 50)


