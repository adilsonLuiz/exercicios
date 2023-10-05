"""  
    Escreva um programa que
    - Leia um numero inteiro
    - Imprima os n primeiros elementos de uma 
    sequencia de fibonacci.

    F = F - 1 + F - 2
    Não consegui realizar este exercicio sozinho.
"""

# Resolução do Guanabara
termos = int(input('Quantos termos você deseja? '))
t1 = 0
t2 = 1
t3 = 0
cont = 3 # Começar a patir do 3 termo

print(f'{t1} -> {t2}', end=' ')

while cont <= termos:
    t3 = t1 + t2
    print(f' -> {t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print()


