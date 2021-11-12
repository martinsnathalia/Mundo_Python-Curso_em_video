# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

f = int(input('Digite um número para calcular o seu fatorial: '))
c = f
fatorial = 1
if f==0:
    print('O fatorial é 1.')
print(f'{f}! = ',end='')
while f != 1:
    print(f'{f} x ',end='')
    fatorial = fatorial*(f-1)
    f = f-1
print('1 = {}.'.format(fatorial*c))

'''Soluções do professor Guanabara:
1)
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial (n)
print ('O fatorial de {} é {}.'.format(n,f))

2)
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
print('Calculando {}! = '.format(n),end = ' ')
while c>0:
    print('{}'.format(c),end = ' ')
    print(' x ' if c>1 else ' = ', end = ' ')
    f *= c
    c -= 1
print('{}'.format(f))
'''


