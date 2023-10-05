# Crie um programa onde o usuario digite um expressão qualquer que user parentese. 
# Seu aplicativo devera analisar se a expressão passada está 
# com os parenteses abertos e fechados na ordem correta.

expressao = list(input('Digite um expressão: '))
parenteses = list()
for element in expressao:
    if element == '(' or element == ')':
        parenteses.append(element)
if parenteses[0] == ')':
    print('Expressão invalida !')
elif parenteses.count('(') == parenteses.count(')'):
    print('Expressão valida !')
else: 
    print('Expressão invalida !')
