# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    tabuada = int(input('Quer ver a tabuada de qual número? '))
    if tabuada < 0:
        break
    for c in range (1,11):
        conta = tabuada*c
        print(f'{tabuada} x {c} = {conta}.')
print('Programa de Tabuada encerrado! Volte sempre!')
