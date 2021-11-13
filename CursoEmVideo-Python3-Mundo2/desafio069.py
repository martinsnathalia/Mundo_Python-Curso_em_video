# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

count0 = count1 = count2 = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA! ')
    print('-'*20)
    idade = int(input('Digite a sua idade: '))
    genero = ' '
    while genero not in 'MFNB':
        genero = str(input('Digite o seu gênero [M, F, NB]: ')).upper().strip()[0]
    if idade >= 18:
        count0 += 1
    if genero == 'M':
        count1 += 1
    if genero == 'F' and idade <= 20:
        count2 += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Você deseja continuar: [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {count0}. \nTotal de homens cadastrados: {count1}. \n'
      f'Total de mulheres com menos de 20 anos {count2}.')


