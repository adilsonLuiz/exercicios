"""  
 Crie um programa que tenha uma tupla com várias palavras 
 (não usar acentos). 
 Depois disso, você deve mostrar, para cada palavra, 
 quais são as suas vogais.
"""

words = (
            'amora', 'pera', 'adilson',
            'linguagem', 'curso', 'onibus',
            'aprender', 'python', 'lancha',
            'comida', 'galileu', 'futuro',
            'mamada'
        )

vogais = ('a', 'e', 'i', 'o', 'u')

for word in words:
    print(f'Na palavra {word.capitalize()} temos ', end='')
    for char in word:
        if char in vogais:
            print(char, end=' ')
    print('\n')

