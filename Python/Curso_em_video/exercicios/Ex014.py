"""  
    Codifique um programa que realize a seguinte ação.
    Realizar a conversão de temperatura de Cº -> Fº
"""

c = float(input('Informe a temperatura Cº: '))

f = (c * 9 / 5) + 32 # Formula da temperatura obtida no google.

print(f'{c}Cº -> {f}Fº')
