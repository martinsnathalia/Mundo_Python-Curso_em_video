# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
# o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
# eles (desconsiderando o flag).

n = 0
count = 0
soma = 0
#n = count = soma = 0   -> poderia fazer assim!
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    soma += n
    count += 1
print('Fim! Ao todo foram digitados {} números e a soma entre eles é de {}.'.format(count-1,soma-999))

'''Poderia fazer dessa forma para não precisar da gambiarra de descontar -1 e -999 do valor total. Dessa forma, 
o valor de 999 não seria contado, pois quando fosse digitado, seria encerrado automaticamente.
n = int(input('Digite um valor [999 para parar]: '))
while n != 999:
    soma += n
    count += 1
    n = int(input('Digite um valor [999 para parar]: '))
print('Fim! Ao todo foram digitados {} números e a soma entre eles é de {}.'.format(count,soma))

# Dessa forma, assim que for digitado 999, o programa não entrará no while e será encerrado de imediato.
'''