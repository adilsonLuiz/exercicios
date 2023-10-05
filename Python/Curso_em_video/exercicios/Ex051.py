"""
    Desenvolva um programa que leia o primeiro termo
    e a razão de uma PA. No final, mostre os 10 primeiros
    termos dessa progressão.
    a10 = a1 + (n - 1)r
"""



primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo_termo = primeiro_termo + (10 - 1) * razao # Formula matematica para resgatar o 10 termo de uma PA

for termo in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{termo} ->', end=' ')
print('FIM')
