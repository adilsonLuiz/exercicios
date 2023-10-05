"""  
 Escreva um programa que 
    - Leia quantidade de Km percorridos por um carro alugado 
    - Leia quantidade de dias pelos quais ele foi alugado.
    - Calcule o preço a pagar (TOTAL), sabendo que; 
     - O carro custa R$60 por dia. 
     - Custo do KM rodado R$0,15.
"""

# Entrada

quantidade_km = float(input('Informe a quantidade de KM rodado com o Carro: '))
quantidade_dia_aluguel = int(input('Informe o total de dias que o carro ficou alugado: '))


# Processamento

total_km_rodado = quantidade_km * 0.15
total_aluguel = quantidade_dia_aluguel * 60
valor_total = total_km_rodado + total_aluguel

# Saida
print(f""" 
    Custo total KM rodado R${total_km_rodado}
    Custo total do aluguel R${total_aluguel}
    Valor total a pagar R${valor_total}
    """)



