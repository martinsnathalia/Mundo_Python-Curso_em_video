# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d = float(input('Digite a distância da sua viagem em km: '))

if d <= 200:
    print('O valor da viagem será de R$ {:.2f}'.format(0.5*d))
else:
    print('O valor da viagem será de R$ {:.2F}'. format(0.45*d))

'''
Outra forma de fazer:
preço = d*0.45 if d > 200 else d*0.50
print('O valor da viagem será de R$ {:.2F}'.format(preço))
'''
