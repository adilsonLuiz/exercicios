"""  
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.

Formula matematica: h² = ca² + co²
Acabei utilizando modulos, mesmo tendo a formula disponivel.
"""

from math import hypot

cateto_adjacente = float(input('Informe o cateto adjacente: '))
cateto_oposto = float(input('Informe o cateto oposto'))

h = hypot(cateto_adjacente, cateto_oposto)

print(f"""  
    Cateto oposto {cateto_oposto}
    Cateto adjacente {cateto_adjacente}
    Hipotenusa {h}
""")
