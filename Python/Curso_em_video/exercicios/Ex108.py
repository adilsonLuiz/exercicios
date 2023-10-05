"""  
Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
que consiga mostrar os números como um valor monetário formatado.
"""

from Ex112 import moeda

valor = int(input('Informe um valor R$'))

print(f'O valor com aumento de 25% fica {moeda.moeda(moeda.aumentar(valor, 25))}')
print(f'O valor com desconto de 30% fica {moeda.moeda(moeda.diminuir(valor, 30))}')
print(f'O dobro de {moeda.moeda(valor)} fica {moeda.moeda(moeda.dobro(valor))}')
