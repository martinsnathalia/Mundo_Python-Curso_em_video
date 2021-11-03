# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))

if n1 == n2:
    print('\33[1:33mNão exite valor maior.\33[m \33[36mAmbos são iguais!\33[m')
elif n1 > n2:
    print('O primeiro valor \33[4:35m{}\33[m é maior que o segundo \33[4:30m{}\33[m!'.format(n1,n2))
else:
    print('O segundo valor \33[1:34m{}\33[m é maior que o primeiro \33[1:32m{}\33[m!'.format(n2,n1))
