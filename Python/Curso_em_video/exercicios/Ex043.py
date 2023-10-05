""" Desenvolva uma logica que leia o 
    peso e altura de uma pessoa e calcule seu IMC
    pesquisar tabela IMC na internet.

"""



people = dict()
people['weigth'] = float(input('Informe seu peso: '))
people['heigth'] = float(input('Informe sua altura: '))
people['imc'] = people['weigth'] / (people['heigth']**2)



print(f'Seu IMC foi {people["imc"]:.1f}')
if people['imc'] < 18.5:
    print('Peso abaixo da media')
elif 18.5 < people['imc'] <= 24.9:
    print('Peso ideal')
elif 24.9 < people['imc'] <= 29.9:
    print('Sobre Peso')
elif 29.9 < people['imc'] <= 34.9:
    print('Obesidade I')
elif 34.9 < people['imc'] <= 39.9:
    print('Obesidade Severa II')
else:
    print('Obesidade Morbida III')