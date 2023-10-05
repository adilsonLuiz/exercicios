def aumentar(valor=0, valor_aumento=0, formatado=True):
    aumento_percentual = (valor * valor_aumento) / 100
    total = valor + aumento_percentual
    return moeda(total) if formatado else total


def diminuir(valor=0, valor_subtracao=0, formatado=True):
    desconto_percentual = (valor * valor_subtracao) / 100
    total = valor - desconto_percentual
    return moeda(total) if formatado else total



def dobro(valor=0, formatado=True):
    valor_dobrado = valor * 2
    return moeda(valor_dobrado) if formatado else valor_dobrado


def metade(valor=0, formatado=True):
    metade_valor = valor / 2
    return moeda(metade_valor) if formatado else metade_valor



def moeda(valor=0):
    valor = str(valor)
    valor = valor.replace('.', ',')
    return f'R${valor}'


def resumo(valor=0, percent_aumento=0, percent_desconto=0):

    print('-' * 40)
    print(f'{"RESUMO DO VALOR".center(40)}')
    print('-' * 40)
    print(f'Preço analisado: \t\t{moeda(valor)}')
    print(f'O dobro do preço: \t\t{dobro(valor)}')
    print(f'{percent_aumento}% de aumento: \t\t{aumentar(valor, percent_aumento)}')
    print(f'{percent_desconto}% de desconto: \t\t{diminuir(valor, percent_desconto)}')
    print('-' * 40)
