# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto em reais: R$ '))
print('O valor do produto com 5% de desconto será {:.2f} reais'.format(preco - (preco * 0.05)))
