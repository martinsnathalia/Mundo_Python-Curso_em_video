# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.

cont = 'S'
count = soma = 0
while cont == 'S':
    num = int(input('Digite um número inteiro: '))
    cont = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    count += 1
    soma += num
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('A média entre todos os {} valores foi de {:.1f}! \n O maior número informado é {} e o menor {}.'.format(count,soma/count, maior, menor))
