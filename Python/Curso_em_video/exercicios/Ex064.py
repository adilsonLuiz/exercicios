"""  
    Crie um programa que
    - Leia varios numeros inteiros
    - Para quando usuário digitar valor 999
    - Imprima total de numeros digitados
    - Imprima soma entre eles desconsiderando o flag
    
"""

sum_number = 0
total_num = 0
end_loop = 999

num = int(input('Informe um número: '))
while num != 999:
    total_num += 1
    sum_number += num
    num = int(input('Informe um número: '))


    

print(f'Você digitou {total_num} numeros, a soma entre eles resultou em {sum_number}')