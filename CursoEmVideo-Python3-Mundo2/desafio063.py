# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma
# Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

seq = int(input('Digite quantos números vc quer ver da sequência de Fibonacci: '))
f1 = 1
f0 = 0
count = 3 # começa em 3 já que os dois primeiros termos serão mostrados antes de entrar no while
print(f0,'→', f1, end=' ')
while count <= seq:
    soma = f1 + f0
    f0 = f1
    f1 = soma
    count += 1
    print('→', soma, end = ' ')
print('→ FIM!')
