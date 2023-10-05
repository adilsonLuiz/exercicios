"""
Exercicio sobre tuplas curso em video

Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, 
de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

#numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
#19, 20)

num_tuple = (
            'Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete',
            'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezeseis',
            'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
            )


num = int(input('Digite um numero de 0 a 20: '))
while num > 20 or num < 0: # Validação de dados
    print('Fora do intervalo.')
    num = int(input('Digite um numero de 0 a 20: '))
print(f'Voce digitou o numero {num_tuple[num]}')
#print('Voce digitou o numero {}' .format(num_tuple[numeros.index(num)]))


