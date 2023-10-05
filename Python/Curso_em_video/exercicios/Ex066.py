"""  
    Crie um programa que
    - Leia varios numeros inteiros
    - Para quando o valor digitado for 999
    - imprimir quantidade de numeros lidos
    - Imprimir soma entre eles
    -  Desconsiderando a flag
"""

"""  
    Para este exercicio não utilizei variaveis compostas (Listas, tuplas e objetos.)
    Pois estava seguindo os junto com a video aula e tentando realizar o exercicio
    com os recursos que havia sido informado no momento
"""
total_sum = total_read_num = 0

while True:
    num = int(input('Informe um número inteiro [Digite 999 para encerrar]: '))
    if num == 999:
        break # Sai do looping
    total_sum += num
    total_read_num += 1

print(f'Total de números lidos {total_read_num}')
print(f'A soma entre todos os valores resultou em {total_sum}')

