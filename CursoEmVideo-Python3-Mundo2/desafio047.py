# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for c in range (2,51,2): #vai contar de 0 a 51, utilizando passo de 2
    print(c, end=' ') #end joga os números para lateral, ao invés de rodar como em uma coluna
print('')
#outra opção:
for c in range(1,51):  #calcular quem é par através do módulo
    if c %2 == 0:
        print(c, end=' ')
