# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
count = 0
ncount = 0
ano_atual = date.today().year
for c in range (0,7):
    data = int(input('Digite a sua data de nascimento: '))
    if ano_atual - data >= 21:
        count = count + 1
    else:
        ncount = ncount + 1
print('{} pessoas já atingiram a maioridade e {} não atingiram!'.format(count, ncount))