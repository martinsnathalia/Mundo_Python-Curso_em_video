# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('Suas retas formam um triângulo?')
r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < (r2+r3) and r2 < (r1 + r3) and r3 < (r2 + r1):
    print('Essas retas formam um triângulo!')
else:
    print('Essas retas NÃO formam um triângulo!')
