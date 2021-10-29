# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
print('O antecessor do número {} é {}'.format(n,n-1))
print('O sucessor do número {} é {} '.format(n,n+1))

#Outra forma de fazer no python

print(f'O antecessor do número {n} é {n-1}')
print(f'O sucessor do número {n} é {n+1}')
