# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
# 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

soma = count = 0
while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break  #com o uso do break, o valor 999 não é somado e a repetição será interrompida.
    soma += n
    count += 1
print(f'A soma dos {count} valores é {soma}.')
