"""  
 Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
 No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.

"""

numbers = (
            int(input('Informe um numero: ')),
            int(input('Informe um numero: ')),
            int(input('Informe um numero: ')),
            int(input('Informe um numero: ')),
        )


print(f'Voce digitou os seguintes valores {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)} vezes')

if 3 in numbers:
    print(f'A posição que o valor 3 apareceu foi {numbers.index(3)}')
else:
    print('O valor 3 não foi digitado')

print('Os numeros pares foram', end=' ')
for number in numbers:
    if number%2 == 0:
        print(number, end=' ')