# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número para saber se é primo: '))

if num == 1:
    print('\33[1:34mEsse número\33[m \33[1:33mNÃO\33[m \33[1:34mé primo!\33[m ')
elif num == 2 or num == 3 or num == 5 or num == 7:
    print('\33[1:32mEsse número\33[m \33[1:36mÉ PRIMO!\33[m')
else:
    s = 0
    for c in range (2,9):
        if num % c == 0:
            s = num+s;
        else:
            s += s;
    if s == 0:
        print('\33[1:32mEsse número\33[m \33[1:36mÉ PRIMO!\33[m')
    else:
      print('\33[1:34mEsse número\33[m \33[1:33mNÃO\33[m \33[1:34mé primo!\33[m ')

'''
#outro jeito:
c = 0
for c in range (2,num):
    if num % c == 0:
        c+=1
if c == 0:
    print('\33[1:32mEsse número\33[m \33[1:36mÉ PRIMO!\33[m')
else:
    print('\33[1:34mEsse número\33[m \33[1:33mNÃO\33[m \33[1:34mé primo!\33[m ')

#outro jeito:

tot=0
for c in range (1, num+1):
    if num % c == 0:
        print('\33[33m', end=' ')
        tot+=1
    else:
        print('\33[36m', end=' ')
    print('{}'.format(c), end='')
print("\n\33[mEsse número é divisível {} vezes.".format(tot))
if tot == 2:
    print('\33[1:32mPor isso, esse número\33[m \33[1:36mÉ PRIMO!\33[m')
else:
    print('\33[1:34mPor isso, esse número\33[m \33[1:33mNÃO\33[m \33[1:34mé primo!\33[m ')
'''