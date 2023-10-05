"""  
    Implemente o Ex061
    Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
    O programa encerrará quando ele disser que quer mostrar 0 termos.

"""

primeiro_termo = int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
termo = primeiro_termo
termo_atual = 0
total_termos = termos_adicionais = 10


while termos_adicionais != 0:
    while termo_atual <= total_termos:
        print(f'{termo} -> ', end=' ')
        termo += razao
        termo_atual += 1

    print('FIM', end='\n')
    termos_adicionais = int(input('Quer mostrar mastrar mais quantos termos? '))
    total_termos += termos_adicionais
print(f'Ao todo foram mostradores {total_termos} termos.')
print('Saindo do programa.')
