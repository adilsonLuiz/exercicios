""" Elabora um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento

- a vista dinheiro ou cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""


valuer_prod = float(input('Informe o preço do produto: '))
print("""Informe o metodo de pagamento.\n
1 - a vista dinheiro ou cheque: 10%% de desconto\n
2 - A vista no cartão: 5%% de desconto\n
3 - em até 2x no cartão: preço normal\n
4 - 3x ou mais no cartão: 20%% de juros\n
""")

payment_method = int(input('Entre com o numero da opção desejada: '))

if payment_method == 1:
    descont =  valuer_prod * 0.10
    final_value = valuer_prod - descont
    print(f'Valor final do produto {final_value}')
elif payment_method == 2:
    descont = valuer_prod * 0.05
    final_value = valuer_prod - descont
    print(f'Voce ira pagar 2x {final_value / 2}')
    print(f'Valor final do produto {final_value}')
elif payment_method == 3:
    final_value = valuer_prod
    print(f'Voce ira pagar 2x R${final_value / 2}')
    print(f'Valor final do produto {final_value}')
elif payment_method == 4:
    parcel_valuer = int(input('Quantas parcelas deseja realizar: '))
    final_value = valuer_prod + (valuer_prod * 0.20)
    print(f'Sua compra foi parcelada em {parcel_valuer}x de {final_value / parcel_valuer}')
    print(f'Acrescentamos 20% de juros e sua compra de {valuer_prod:.2f} ficou em {final_value:.2f}')
else:
    print(f'Opção invalida, tente novamente.')




