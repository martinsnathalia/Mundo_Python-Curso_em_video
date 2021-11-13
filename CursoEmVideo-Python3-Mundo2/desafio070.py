# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('-' * 13)
print('LOJA DA NATH!')
print('-'*13)
price = count1 = count2 = 0
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preço = int(input('Digite o preço: '))
    price += preço
    count2 += 1
    if preço > 1000:
        count1 += 1
    if count2 == 1 or preço < menor:
        menor = preço
        produto = nome
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Você deseja continuar: [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
print(f'Valor total gasto: {price}.\n'
      f'Total de produtos acima de R$ 1000: {count1}.\n'
      f'O produto de menor valor é a(o) {produto} que custa R$ {menor:.2f}.')