# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base
# de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
conversão = int(input('Agora escolha uma base de conversão: \n 1 - Binário \n 2 - Octal \n 3 - '
                      'Hexadecimal \n Digite o número correspondente a base escolhida:  '))

b = bin(num)
h = hex(num)
o = oct(num)

if conversão == 1:
    print('O número {} será equivalente a {} em binário!'.format(num,b[2:])) #fatiamento: pegará do 2 em diante
elif conversão == 2:
    print('O número {} será equivalente a {} em octal!'.format(num,o[2:]))
elif conversão == 3:
    print('O número {} será equivalente a {} em hexadecimal!'.format(num,h[2:]))
else:
    print('Não será possível fazer a conversão pois não há correspondência para o valor [{}] digitado.'.format(conversão))