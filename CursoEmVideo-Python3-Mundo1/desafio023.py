# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número entre o intervalo de 0 a 9999: '))

print('A unidade é {}'.format(num//1%10))
print('A dezena é {} '.format(num//10%10))
print(f'A centena é {num//100%10}')
print(f'O milhar é {num//1000%10}')

#n = int(input('Digite um número entre 0 e 9999: '))
#n2 = str(int(10000 + n))
#print('O número {} possui, {} milhares.'.format(n, n2[1]))
#print('O número {} possui, {} centenas. '.format(n, n2[2]))
#print('O número {} possui, {} dezenas. '.format(n, n2[3]))
#print('O número {} possui, {} unidades.'.format(n, n2[4]))

