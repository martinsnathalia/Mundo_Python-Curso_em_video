# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
# do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

age = 0
count = 0
velho = 0
for c in range (1,5):
    nome = str(input('Digite o seu nome: ')).upper().strip()
    idade = int(input('Digite a sua idade: '))
    genero = str(input('Digite o seu gênero [M, F, NB]: ')).upper().strip()

    age += idade
    if idade < 20 and genero == 'F':
        count = count+1
    if genero == 'M' and idade > velho:
        nomevelho = nome
        velho = idade
print('A média de idade no grupo é de {:.2f} anos.'.format(age/4))
print('{} mulheres possuem idade inferior a 20 anos.'.format(count))
print('O homem mais velho tem o nome {} e possui {} anos'.format(nomevelho,velho))



