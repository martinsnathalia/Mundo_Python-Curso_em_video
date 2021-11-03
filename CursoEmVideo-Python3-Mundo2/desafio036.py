# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.

from time import sleep
print(12*'>*<')
print('\33[1:32:107mAPROVAÇÃO PARA EMPRÉSTIMO BANCÁRIO\33[m')
print(12*'>*<')
sleep(1)
casa = float(input('Qual é o valor da casa que você quer comprar? '))
salário = float(input('Quanto é o seu salário? '))
anos = int(input('Quantos anos você pretende demorar a pagar? '))

meses = anos*12
pgto = casa/meses
min = 0.30*salário

if pgto <= min:
    print('Você deverá pagar mensalmente por {} anos o valor de R$ {:.2f}. Empréstimo concedido!'.format(anos,pgto))
else:
    print('A parcela será de {:.2f}, maior que 30% do seu salário {:.2f}. Infelizmente você não poderá '
          'receber esse empréstimo!'.format(pgto,min))

