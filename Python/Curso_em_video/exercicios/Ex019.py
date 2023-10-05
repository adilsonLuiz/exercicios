"""  
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""


from random import choice

names = ['Lucas', 'Adilson', 'Moises', 'Jucelino']


print(f'O aluno escolhido para escrever no quadro foi {choice(names)}')