"""
    Codifique um programa que mostre na tela todos
    os números pares que estão no intervalo entre 1 e 50
"""


""" 
    for pares in range(1, 51): # Ira ser executado 50 vezes independentemente se for um numero par ou nao
        if pares % 2 == 0: # Se o resto da divisão do valor da variavel de controle no momento for igual a zero
            print(f'{pares} ', end='')
    print()
"""

""" 
    O codigo acima se torna pesado, por conta que o laço e executado muitas
    vezes de forma desnecessaria, podemos melhorar a eficiencia pulando os 
    laços desnecessarios utilizando a pripria função range.
""" 


# Exemplo de com codigo mais eficiente
# Este codigo e mais eficiente pois dentro da função range especificamos que queremos andar em 2 unidades.
# Desta forma a iteração ira executar de forma mais leve pois ira ser feito menos laçoes do que antes
# Será feito a metado dos laços e não todo os 50 laçõs
pares = [ par for par in range(2, 51, 2) ]

print(pares)