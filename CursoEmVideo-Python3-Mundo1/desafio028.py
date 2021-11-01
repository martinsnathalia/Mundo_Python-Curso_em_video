# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

import random
from time import sleep

n = random.randint(0,5)  # ou random.choice([0,1,2,3,4,5]) - o pc vai pensar em um número de 0 a 5
print('-=-'*18)
print('Vou pensar em um número de 0 a 5, tente adivinhar...')
print('-=-'*18)
sleep(1) # faz o programa esperar 1 segundos
a = int(input('Que número você acha que eu pensei? \nR: '))
print('PROCESSANDO...')
sleep(1)
if a == n:
    print('Parabéns! Você acertou! Já pode jogar na mega...')
else:
    print('Errou, querida. Eu pensei em {} e vc chutou {}. Tente outra vez!'.format(n,a))



