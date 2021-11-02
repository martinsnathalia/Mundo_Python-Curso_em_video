# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
a = int(input('Digite um ano qualquer para saber se ele é bissexto: '))

if a == 0:
    a = date.today().year   # para pegar o ano atual, só digitar "0"

if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print(f'O ano {a} é bissexto!')
else:
    print('Esse ano NÃO é bissexto!')


# Ano bissexto = tem que ser divisível por 4 e não pode ser divisível por 100 ou o ano deve ser divisível por 400



