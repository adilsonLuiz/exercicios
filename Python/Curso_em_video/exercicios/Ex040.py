""" - Leia duas notas de um aluno
	- Calcule sua media
	- Imprimir mensagem de acordo com a media

	< 5.0 REPROVADO
	>= 5.0 e <= 6.9 RECUPERAÇÂO
	> 7.0 APROVADO
"""


notas = list()
notas.append(float(input('Informe a primeira nota: ')))
notas.append(float(input('Informe a segunda nota: ')))
media = sum(notas) / 2


if media < 5:
	print(f'Media: {media} \033[1;31mREPROVADO\033[m')
#elif media >= 5 and media <= 6:
elif 7 >= media >= 5:
	print(f'Media: {media} \033[1;33mRECUPERAÇÂO\033[m')
else:
	print(f'Media: {media} \033[1;32mAPROVADO\033[m')