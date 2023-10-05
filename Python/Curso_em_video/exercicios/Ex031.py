"""  
Desenvolva um programa que 
Entrada
    - Leia distância de uma viagem em Km. 
Processamento
    - Calcule o preço da passagem
    OBS 
        - R$0,50 por Km para viagens de até 200Km
        - R$0,45 para viagens mais longas.
Saida
    - Exiba o valor a ser pago
"""

distance = int(input('Qual foi a distancia percorrida: '))

if distance < 200:
    total_valuer_pay = distance * 0.50
else:
    total_valuer_pay = distance * 0.45

print(f'Para a distancia de Km{distance} rodado, voce pagara R${total_valuer_pay}')



