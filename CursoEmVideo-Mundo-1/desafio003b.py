# Crie um programa que leia dois números e mostre a soma entre eles | Outra sintaxe

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
soma = a + b
#print('A soma entre ',a,'e',b,'é ', soma)
print('A soma entre {0} e {1} vale {2}'.format(a,b,soma))
