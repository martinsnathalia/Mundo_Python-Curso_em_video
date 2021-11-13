# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print('='*25)
print('VAMOS JOGAR PAR OU ÍMPAR? ')
print('='*25)
count0 = count1 = 0
while True:
    jogador = int(input('Digite um valor: '))
    pc = randint(0,10)
    soma = jogador + pc
    jogada = ' '
    while jogada not in 'PpIi':
        jogada = str(input('Par ou Ímpar? [P/I] ')).strip()[0]
    if jogada in 'Pp':
        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador {pc}. A soma deu {soma}.')
            print('Parabéns você VENCEU! Vamos jogar de novo!')
            count0 += 1
        else:
            break
    if jogada in 'Ii':
        if soma % 2 != 0:
            print(f'Você jogou {jogador} e o computador {pc}. A soma deu {soma}.')
            print('Parabéns você VENCEU! Vamos jogar de novo!')
            count1 += 1
        else:
            break
print(f'Você jogou {jogador} e o computador {pc}. A soma deu {soma}.')
print(f'Você PERDEU! Foram {count0+count1} vitórias consecutivas!')


