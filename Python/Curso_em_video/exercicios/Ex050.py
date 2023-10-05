"""
    Desenvolva um programa que leia seis números inteiros
    e mostre a soma apenas daqueles que forem pares.
    Se o valor digitado for impar, desconsidere-o.

    - ler 6 numeros inteiros
    - mostrar soma de pares
    - descartar impares
    - exibir resultado

"""


somatorio = 0
quantidade_numeros_lido = 0
 
for number in range(1, 7):
    number = int(input('Informe um numero: '))
    if number%2 == 0:
        somatorio += number
        quantidade_numeros_lido += 1


print(f'Resultado da soma de pares {somatorio}')
print(f'Total de numeros PARES lidos {quantidade_numeros_lido}')
