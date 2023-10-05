"""
Codifique um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com o 
tamanho adaptável.
Ex:
escreva('Ola mundo!')

Saida:
~~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~~
"""


def write_msg(border, word):
    if border == '':
        border = '~'
    extra_border_number = 2
    text_center_ailing = (len(word) + extra_border_number)
    print(border * (len(word) + extra_border_number))
    print(f'{"".join(word).capitalize():^{text_center_ailing}}')
    print(border * (len(word) + extra_border_number))


# Main code here

word_print = list(str(input('Escreva algo: ')))
border_line = str(input('Linha: '))
write_msg(word_print, border)
