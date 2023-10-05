"""  
Crie um programa que tenha a função leiaInt(), 
que vai funcionar de forma semelhante ‘a função input() 
do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
Ex: n = leiaInt(‘Digite um n: ‘)
"""


def leia_int(txt):
    try: 
        action = int(input(txt))
    except ValueError:
        action = 'Erro, somente valores  numeros aceitos'
    return action


n = leia_int('Informe um numero: ')
print(n)
