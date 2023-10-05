""" Escreva um programa que

- Leia um numero inteiro qualquer
- Peça para o usuário escolher a base da conversão

Baseado na escolha, converta

- 1 Binario
- 2 Octal
- 3 Hexadecimal 

"""








number_to_convert = int(input('Informe um número qualquer para conversão: '))

print(
    """ 
    - 1 Binario
    - 2 Octal
    - 3 Hexadecimal
    """
    )
convert_type = int(input('Escolha: '))

if convert_type == 1:
    print(f'{number_to_convert} em Binario é {bin(number_to_convert)[2:]}')
elif convert_type == 2:
    print(f'{number_to_convert} em Octal é {oct(number_to_convert)[2:]}')
elif convert_type == 3:
    print(f'{number_to_convert} em Hexadecimal é {hex(number_to_convert).upper()[2:]}')
else:
    print(f'Opção invalida tentar novamente!!')
    
