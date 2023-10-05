"""  
Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota  
- A média da turma
- A situação (opcional)
"""


def notas(*notas_aluno, situacao=False):
    from math import trunc

    dados_alunos = dict()
    dados_alunos['total_notas'] = len(notas_aluno)
    dados_alunos['maior_nota'] = max(notas_aluno)
    dados_alunos['menor_nota'] = min(notas_aluno)
    dados_alunos['media_turma'] = trunc(sum(notas_aluno) / len(notas_aluno))
    if situacao:
        if dados_alunos['media_turma'] < 5:
            dados_alunos['situação_turma'] = 'RUIM'
        elif 5 < dados_alunos['media_turma'] <= 6:
            dados_alunos['situação_turma'] = 'MEDIANA'
        else:
            dados_alunos['situação_turma'] = 'OTIMA'
    return dados_alunos


resultado = notas(5.5, 9.5, 10, 6.5, situacao=True)
print(resultado)
