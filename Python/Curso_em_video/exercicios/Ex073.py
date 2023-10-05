"""  
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.

"""

times_brasileirao = (
                    'internacional', 'flamento', 'atletico-mg',
                    'sao paulo', 'fluminense', 'gremio',
                    'palmeiras', 'corinthians', 'chapecoense',
                    'athletico-pr', 'santos', 'ceara',
                    'atletico-go', 'sport', 'fortaleza',
                    'bahia', 'vasco', 'goias', 'coritiba',
                    'botafogo'
                    )

print('-=' * 20)
print('\tTABELA TIMES BRASILEIRÃO')
print('-=' * 20)
for index, time in enumerate(times_brasileirao):
    print(f'{index + 1}º Colocação - {time.capitalize()}')

print('\n')
print(f'Os cincos primeiros times são,')
for time in times_brasileirao[0:5]:
    print(time.capitalize())

print('\n')
print(f'Os ultimos 4º colocados são,')
for time in times_brasileirao[-4:]:
    print(time.capitalize())

print('\n')
print('Times em ordem alfabetica,')
for time in sorted(times_brasileirao):
    print(time.capitalize())

print('\n')
print(f'O time da Chapecoense esta na posição: {times_brasileirao.index("chapecoense")}')