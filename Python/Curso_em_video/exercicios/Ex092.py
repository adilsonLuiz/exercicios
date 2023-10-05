"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferete de ZERO,
o dicionário receberá também o ano de contratação e o salario. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar
"""

from datetime import date

ano_atual = date.today().year
trabalhador = dict()


trabalhador['nome'] = str(input('Informe seu nome: '))
trabalhador['ano_nascimento'] = int(input('Data de nascimento: '))
trabalhador['idade'] = ano_atual - trabalhador['ano_nascimento']


print('''
        [Digite o numero] - Possuo Carteira de trabalho.
        [0] - Não possuo carteira de trabalho.
    '''
    )
trabalhador['numero_ctps'] = int(input('Digite uma opção: '))

if trabalhador['numero_ctps'] != 0:
    trabalhador['ano_de_contratacao'] = \
        int(input('Informe o ano que foi contratado: '))
    trabalhador['salario'] = float(input('Informe o sálario nesta contratação: '))
    trabalhador['idade_restante_aposentar'] = 65 - trabalhador['idade']
    trabalhador['ano_restante_aposentar'] = \
                trabalhador['idade_restante_aposentar'] + ano_atual
    print(f''' 
    O trabalhador {trabalhador["nome"]}, tem {trabalhador["idade"]} anos de idade.
    Ainda resta {trabalhador["idade_restante_aposentar"]} anos até a aposentadoria.
    Você poderá se aposentar no ano de {trabalhador["ano_restante_aposentar"]}.
    Numero da CTPS: {trabalhador["numero_ctps"]}''')
else:
    print(f'''
    {trabalhador["nome"]}, voce possui {trabalhador["idade"]} anos de idade.
    Você não possui trabalho, por isso, não contribuiu para aposentadoria.
    ''')



