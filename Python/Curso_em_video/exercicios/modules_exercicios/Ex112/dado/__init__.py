def leia_dinheiro(txt):
    while True:
        valor = input(txt).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'ERRO! o valor "{valor}" não e valido')
        else:
            return float(valor)

                    