# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
b = float(input('Digite o comprimento do cateto oposto: '))
c = float(input('Digite o comprimento do cateto adjacente: '))
soma = math.pow(b,2) + math.pow(c,2)
print('A hipotenusa é = {}'.format(math.sqrt(soma)))
# utilizando outra forma para obter a hipotenusa
print('A hipotenusa é = {:.2f}'.format(math.hypot(b,c)))