# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

from time import sleep
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

média = (n1+n2)/2

print(f'Sua média é {média:.1f}')
sleep(0.5)
if média >= 7:
    print("Parabéns! Você está aprovado!")
elif média >= 5 and média <= 6.9:
    print('Atenção! Você está de recuperação!')
else:
    print('Infelizmente você está reprovado!')
