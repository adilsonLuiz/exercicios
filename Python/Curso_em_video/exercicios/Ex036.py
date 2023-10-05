"""escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. 

- Programa deve perguntar valor da casa
- Programa deve perguntar o salario do comprador
- Perguntar quantos anos ele vai pagar

A saida devera ser o calculo do valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo
será negado """ 

from math import ceil


house_price = float(input('Informe o valor da casa: '))
money = float(input('Informe o seu salario: '))
year_pay = int(input('Informe total de anos que o pagamento será efetivado: '))

# Multiplicar a quantidade de anos por 12 para obter o total de meses.

price_month = house_price / (year_pay * 12)

if price_month >= money * 0.3:
    print(f'O valor da parcela é de R${ceil(price_month)} e excede 30% de seu salario.')
    print('Emprestimo recusado.')
else:
    print(f'Emprestimo aprovado')
    print(f'Você pagará R${int(price_month)} x {year_pay * 12}.')
