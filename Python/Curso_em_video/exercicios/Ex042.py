""" Refaça o ex 35 e adicione a seguinte implementação

	- Equilátero: todos os lados iguais
	- Isósceles: dois lados iguais
	- Escaleno: todos os lados diferentes

"""
# Triangulo v2.0

reta1 = float(input('Informe o primeiro seguimento: '))
reta2 = float(input('Informe o segundo seguimento: '))
reta3 = float(input('Informe o terceiro seguimento: '))


if reta1 < reta2 + reta3 and reta1 > abs(reta2 - reta3):
	print('Com essas medidas podemos fazer um triangulo ', end='')
	#if reta1 == reta2 and reta2 == reta3:
	if reta1 == reta2 == reta3:
		print('Equilátero')
	elif reta1 != reta2 != reta3 != reta1:
		print('Escaleno')
	else:
		print('Isósceles')
else:
	print('Com essas medidas não podemos fazer um triangulo')