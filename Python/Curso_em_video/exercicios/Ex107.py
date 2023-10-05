"""
 Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
 Faça também um programa que importe esse módulo e use algumas dessas funções.
"""


from Ex112 import moeda

valor = float(input('Digite um valor R$'))


print(f'O valor com aumento de 10% fica {moeda.aumentar(valor, 10)}')
print(f'O valor com 20% de desconto fica {moeda.diminuir(valor, 20)}')
print(f'O dobro do valor fica {moeda.dobro(valor)}')
print(f'A metade do valor {moeda.metade(valor)}')