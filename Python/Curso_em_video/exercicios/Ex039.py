""" 

Entradas
    - Leia o ano de nascimento 

Processamento
    - Verificar estado de alistamento do usuario
        - Se não esta no tempo
            - Calcular quanto tempo falta para se alista
            - Informar ao usuario resultados
        - Se esta no tempo
            - Informar que esta no tempo de engresso ao serviço militar
        - Se tempo passou
            - Calcular quanto tempo excedeu do alistamento
            - Informar ao usuario resultados
        
Saida
- Informe dados de acordo com a condição
 
"""
from datetime import date


# Desafio extra sugerido pelo professo, realizar a leitura do sexo.
sexo = str(input('Sexo: (F\M): ')).strip().upper()

# Procurei colocar a chagem do sexo logo antes de qualquer calculo ou declaração
# Tendo em vista, que o resultado pode encerrar o programa de imediato, salvando recusos computacionais.
if sexo == 'F': 
    print('Por ser mulher, você não precisa realizar alistamento')
    exit(0)


ano_atual = date.today().year
ano_nascimento = int(input('Informe o ano de nascimento: '))
idade = ano_atual - ano_nascimento
idade_maxima_alistamento = 19

# Calculando a idade que falta para alistamento
if idade < idade_maxima_alistamento:
    anos_ate_alistamento = idade_maxima_alistamento - idade # Anos faltantes até o alistamento.
    alistamento =  ano_nascimento + anos_ate_alistamento # Ano que alistamento ocorrera
elif idade > idade_maxima_alistamento: # Calculando o tempo execido do alistamento
    anos_excedido_alistamento = idade - idade_maxima_alistamento
    ano_de_alistamento = ano_atual - anos_excedido_alistamento

if idade < idade_maxima_alistamento:
    print(f'Voce ainda não pode se alistar, pois possui {idade} anos.')
    print(f'Ainda falta {anos_ate_alistamento} para voce se alistar.')
    print(f'Voce poderá se alista no ano de {alistamento}')
elif idade == idade_maxima_alistamento:
    print(f'Voce possui {idade} anos')
    print(f'Corra para realizar seu alistamento.')
else:
    print(f'Voce já passou da idade maxima de alistamento, sua idade {idade}')
    print(f'Anos que passaram até a data de alistamento {anos_excedido_alistamento}')
    print(f'Ano que voce deveria ter feito o alistamento {ano_de_alistamento}')
    




