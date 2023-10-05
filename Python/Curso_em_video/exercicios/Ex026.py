"""  
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
"""

frase = input('Digite uma frase: ').strip().upper()


print(f'''
        Frase: {frase.capitalize()}
        Total de letras "A": {frase.count('A')}
        Primeira aparição : {frase.find('A')}
        Ultima aparição: {frase.rfind('A')}
    ''')