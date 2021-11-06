# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maior = 0
menor = 1000

for c in range (1,6):
    peso = float(input(f'Digite o {c}º peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso listado é {} kg e o menor é {} kg.'.format(maior,menor))

'''
#outra opção para não colocar o menor com um teto
maior = 0
menor = 0
for c in range (1,6):
    peso = float(input('Digite o seu peso: '))
    if c == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso listado é {} kg e o menor é {} kg.'.format(maior,menor))

#outra maneira:
pesos = [ ]
for p in range(0,5):
    peso = float(input('Digite o peso: '))
    pesos.append(peso)
    print(pesos)
print('O maior peso é {}Kg' .format(max(pesos)))
print('O menor peso é {}Kg' .format(min(pesos)))
'''