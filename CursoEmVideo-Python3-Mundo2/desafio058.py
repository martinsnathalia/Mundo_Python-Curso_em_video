# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

print('-=-'*18)
print('Vou pensar em um número de 0 a 10, tente adivinhar...')
print('-=-'*18)
n = random.randint(0, 10)  # ou random.choice([0,1,2,3,4,5]) - o pc vai pensar em um número de 0 a 10
count = 0
'''a=11
while a!=n:
    a = int(input('Que número você acha que eu pensei? '))
    count+=1
print('Você acertou! Levou {} tentativas para acertar!'.format(count))

#outra opção do professor:'''
acertou = False
while not acertou:
    jogador = int(input('Que número você acha que eu pensei? \nR: '))
    count+=1
    if jogador == n:
       acertou = True
    else:
        if jogador < n:
            print('Mais...Tente mais uma vez!')
        else:
            print('Menos...Tente mais uma vez!')
print('Você acertou! Levou {} tentativas para acertar!'.format(count))
