""" Escreva um programa que

- Leia dois números inteiros
- Compare-os monstrando na tela uma mensagem

A mensagem deve conter

- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais """


numbers = [
            int(input('Informe um numero: ')), 
            int(input('Informe outro numero: '))
            ]


if numbers[0] > numbers[0 + 1]:
    print('O primeiro valor e maior')
elif numbers[0] < numbers[0 + 1]:
    print('O Segundo valor e maior')
else:
    print('Não existe valores iguais, os dois são iguais')