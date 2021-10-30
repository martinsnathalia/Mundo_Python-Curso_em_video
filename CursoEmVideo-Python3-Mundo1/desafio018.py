# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
a = float(input('Digite o ângulo para saber o seno, cosseno e tangente: '))
r = math.radians(a) #converte para radianos
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(math.sin(r), math.cos(r), math.tan(r)))
