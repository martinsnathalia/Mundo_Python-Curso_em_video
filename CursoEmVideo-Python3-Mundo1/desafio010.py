# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print('Conversão Real para Dólar!')
r = float(input('Quantos reais você possui na carteira? R$: '))
d = r/5.37
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(r,d))
