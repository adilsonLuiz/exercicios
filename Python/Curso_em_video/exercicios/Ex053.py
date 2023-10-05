"""
    Crie um programa que leia um frase qualquer e diga
    se ela é um palíndromo, desconsiderando os espaços

    - ler uma palavra
    - gravar em uma variavel a palavra escrita ao contrario
    - verificar se as 2 palavras são iguais
"""

# Palavra original de entrada

word = str(input('Informe um palavra: ')).strip().upper()


# Processamento
word = word.replace(' ', '') # Removendo espaço da string original.
reverse_word = word[::-1] # Obtendo a palavra ao contrario realizando um slicing na string.



if word == reverse_word:
    print(f'O inverso de {word} é {reverse_word}')
    print(f'A palavra "{word}" é um palindromo.')
else:
    print(f'O inverso de {word} é {reverse_word}')
    print(f'A palavra "{word}" não é um palindromo')






