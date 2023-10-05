""" A Confederação Nacional de Natação precisa de um programa que 
	leia o ano de nascimento de um atleta e mostre sua categoria, 
	de acordo com a idade:
	
	até 9 anos: mirim
	até 14: infantil
	até 19: junior
	até 25: senior
	acima: master 

"""


from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Entre com sua data de nascimento: '))
idade = ano_atual - ano_nascimento

if idade <= 9:
	print(f'O atleta tem {idade} anos')
	print('Categaria mirim')
elif idade <= 14:
	print(f'O atleta tem {idade} anos')
	print('Categoria Infantil')
elif idade < 20:
	print(f'O atleta tem {idade} anos')
	print('Categoria Junior')
elif idade <= 25:
	print(f'O atleta tem {idade} anos')
	print('Categoria Senior')
else:
	print(f'O atleta tem {idade} anos')
	print('Categoria Master')