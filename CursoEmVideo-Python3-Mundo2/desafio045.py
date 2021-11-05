# Crie um programa que faça o computador jogar Jokenpô com você.

import random #random e choice = para string. Poderia ter usado random e randint para inteiros e trabalhar com inteiros para representar as opções
from time import sleep
#from random import randint
#itens = ['Pedra', 'Papel', 'Tesoura']
#computador = randint(0,2)
#print('O computador escolheu {}'.format(itens[computador]))
print('\33[4:31m<*>\33[m'*7)
print(' \33[1:33mVAMOS JOGAR JOKENPÔ?\33[m')
print('\33[4:31m<*>\33[m'*7)
sleep(1)
jogo = ['pedra', 'papel', 'tesoura']

vc = str(input('Faça a sua escolha: Pedra, Papel ou Tesoura. Vamos ver se será capaz de me vencer: ')).strip()
user = vc.lower() # converterá a resposta do user para minúsculo, para comparar com o "jogo", que tá em minúsculo.
user2 = vc.upper() # coloquei maiúsculo apenas para usar no PRINT e destacar.
print('\33[1:35mJO\33[m')
sleep(0.5)
print('\33[1:35mKEN\33[m')
sleep(0.5)
print('\33[1:35mPÔ\33[m')
sleep(0.5)

pc = random.choice(jogo)
pc1 = pc.upper()

if user == pc:
    print("Eu joguei {} e você jogou {}.\33[1:33mEMPATAMOS!\33[m ".format(pc1,user2))
elif user == 'pedra' and pc == 'tesoura':
    print('\33[1:34mYOU WIN!\33[m Eu escolhi {}, você {}. Parabéns!'.format(pc1, user2))
elif user == 'pedra' and pc == 'papel':
    print('\33[1:32mHAHAHA EU GANHEI!\33[m Você escolheu {}, eu escolhi {}. Tenta de novo, noob!'.format(user2,pc1))
elif user == 'tesoura' and pc == 'papel':
    print('\33[1:34mYOU WIN!\33[m Eu escolhi {}, você {}. Parabéns!'.format(pc1, user2))
elif user == 'tesoura' and pc == 'pedra':
    print('\33[1:32mHAHAHA EU GANHEI!\33[m Você escolheu {}, eu escolhi {}. Tenta de novo, NOOB!'.format(user2,pc1))
elif user == 'papel' and pc == 'tesoura':
    print('\33[1:32mHAHAHA EU GANHEI!\33[m Você escolheu {}, eu escolhi {}. Tenta de novo, noob!'.format(user2,pc1))
elif user == 'papel' and pc == 'pedra':
    print('\33[1:34mYOU WIN!\33[m Eu escolhi {}, você {}. Parabéns!'.format(pc1, user2))
elif user != 'pedra' or user != 'papel' or user != 'tesoura':
    print('Essa não é uma opção válida!')
print('\33[4:36mVAMOS JOGAR DE NOVO?\33[m')
