# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = 0
while c != 5:
    print('Menu: \n [1] somar; \n [2] multiplicar; \n [3] maior; \n [4] novos números; \n [5] sair do programa')
    c = int(input('Digite qual operação deseja realizar: '))
    if c == 1:
        print('A soma dos números {} e {} é: {}.'.format(a,b,a+b))
    elif c == 2:
        print('A multiplicação dos números {} e {} é: {}.'.format(a, b, a*b))
    elif c == 3:
        print('O maior número entre {} e {} é: {}.'.format(a, b, max(a,b)))
    elif c == 4:
        print('Você deverá digitar novos números!')
        a = int(input('Digite um valor: '))
        b = int(input('Digite outro valor: '))
    elif c == 5:
        print('Você sairá do programa!')
    else:
        print('Essa não é uma opção válida!')




