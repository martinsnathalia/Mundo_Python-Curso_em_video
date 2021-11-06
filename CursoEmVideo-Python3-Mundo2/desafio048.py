# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for c in range (1,501):
    if c%2 != 0:
        if c%3 == 0:
            soma += c   #acumulador: vai acumulando os dados solicitados
            cont = cont + 1 #contador: vai contando a quantidade dos itens solicitados
print('A soma de {} números ímpares do intervalo de 1 a 500 é de: {}'.format(cont, soma))

#outra opção:
soma2 = 0
cont2 = 0
for c in range (1,501,2):
    if c%3 == 0:
        soma2 = soma2 + c
        cont2 = cont2 + 1
print('Soma de {} números é de {}'.format(cont2,soma2))

