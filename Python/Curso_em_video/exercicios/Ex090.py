"""
Faça um programa que leia nome e média de um aluno, guardando também a situação
em um dicionario. No final, mostre o conteúdo da estrutura na tela
"""

aluno = dict()

aluno['nome'] = str(input('Nome do aluno: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] < 4:
    aluno['situacao'] = 'Reprovado'
elif 4 < aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'
for key, valuer in aluno.items():
    print(f'O {key} é igual a {valuer}')
