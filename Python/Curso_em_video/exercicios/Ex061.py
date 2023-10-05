"""  
    Refaça o ex 051, usando a estrutura while

"""

primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo_atual = primeiro_termo
cont = 0



while cont <= 10:
    print(f'{termo_atual} -> ', end=' ')
    termo_atual += razao
    cont += 1
print('FIM', end=' ')