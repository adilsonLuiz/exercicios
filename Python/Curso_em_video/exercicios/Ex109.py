""" 
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
"""

from Ex112 import moeda

valor = float(input('Informe um valor R$'))

print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor)}')