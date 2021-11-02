# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a > b:
    if a > c:
        print('O número {} é o maior número.'.format(a))
        if b > c:
            print('O número {} é o menor número.'.format(c))
        else:
            print('O número {} é o menor número.'.format(b))
    else:
        print('O número {} é o maior número.'.format(c))
        print('O número {} é o menor número.'.format(b))
else:
    if b > c:
        print('O número {} é o maior número.'.format(b))
        if a > c:
            print('O número {} é o menor número.'.format(c))
        else:
            print('O número {} é o menor número.'.format(a))

    else:
        print('O número {} é o maior número.'.format(c))
        print('O número {} é o menor número.'.format(a))

'''
Resolução do Guanabara:

menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
'''