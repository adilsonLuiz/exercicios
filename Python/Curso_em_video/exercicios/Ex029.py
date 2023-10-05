"""
    Escreva um programa que

    Entradas
        - leia a velocidade de um carro. 
    Processamento\Saida
        -Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 

    obs:A multa vai custar R$7,00 por cada Km acima do limite.

"""


speed_car = int(input('Informe a velocidade atual: '))

if speed_car > 80:
    print(f'Voce foi multado por estar a {speed_car}Km em uma pista de 80Km')
else:
    print(f'Otimo, voce esta no limite de velocidade')