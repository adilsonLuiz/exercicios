"""  
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

n1 = int(input('Informe um numero: '))
n2 = int(input('Informe outro numero: '))
n3 = int(input('Informe outro numero: '))

#TODO fazer sem condinção aninhada.

maior = menor = n1

if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'O menor valor foi {menor}')
print(f'O maior valor foi {maior}')





