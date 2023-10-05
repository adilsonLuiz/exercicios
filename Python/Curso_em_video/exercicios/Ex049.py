"""
Refaça o desfio 009, mostrando o número que o usuário 
escolher, só que agora utilizando iteração for
"""

"""  
Faça um programa que leia um numero qualquer e mostre na tela a sua tabuada.
"""

tabuada_num = int(input('Informe um numero: '))
for tab_num in range(0, 11):
    print(f'{tabuada_num} x {tab_num} = {tabuada_num * tab_num}')