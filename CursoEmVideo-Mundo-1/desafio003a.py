# Crie um programa que leia dois números e mostre a soma entre eles.

a=int(input('Digite um número: ')) # input entende o dado como string, logo, vai entender os valores como letras
b=int(input('Digite outro número: '))
soma = a + b # por isso, usa-se o "int" para converter o dado em número
print('A soma é ', soma)
