"""  
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

Irei utilizar modulos, tendo em vista que a proposta da aula foi sobre módulos em Python
"""



from math import sin, cos, tan

angule = float(input('Informe um angulo qualquer: '))

print(f"""  
    Seno: {sin(angule)}
    Cosseno: {cos(angule)}
    Tangente: {tan(angule)}
""")