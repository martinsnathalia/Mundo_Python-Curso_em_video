# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format('  LOJAS CAVALCANTI  '))
preço = float(input('Qual é o preço do produto? \nR: '))
condição = int(input('Qual será a condigação de pagamento: \n [1] À vista em \33[1:34mdinheiro/cheque\33[m '
                     '\n [2] \33[1:34mÀ vista no cartão\33[m \n [3] \33[1:34m2x no cartão\33[m '
                     '\n [4] \33[1:34m3x ou mais no cartão\33[m \n Informe: '))

if condição == 1:
    print("O valor a ser pago será R$ {}".format(0.9*preço))
elif condição == 2:
    print('O valor a ser pago será R$ {}'.format(0.95*preço))
elif condição == 3:
    print('O valor a ser pago será R$ {}'.format(preço))
elif condição == 4:
    print('O valor a ser pago será R$ {}'.format(1.20*preço))
else:
    print('Essa não é uma opção válida!')

