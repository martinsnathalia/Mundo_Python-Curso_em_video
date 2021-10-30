# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc, floor
num = float(input("Digite um número qualquer para saber sua porção inteira: "))
inteiro = floor(num)
print ('A porção inteira desse número é {}!'.format(inteiro))


# outra forma de fazer utilizando a função trunc que corta a parte inteira do número
print ('A porção inteira de {} é {}!'.format(num, trunc(num)))
# outra forma sem importar função, apenas utilizando a parte inteira do número, com "int"
print ('A porção inteira de {} é {}!'.format(num, int(num)))
