"""  
Dentro do pacote Ex112 que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), 
mas com uma validação de dados para aceitar apenas valores que seja monetários.
"""

from Ex112 import moeda
from Ex112 import dado

valor = dado.leia_dinheiro('Informe um valor R$')

moeda.resumo(valor, 10, 20)
