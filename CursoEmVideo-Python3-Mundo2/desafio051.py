# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))

for c in range (1,11):
    d = a + (c-1)*r
    print('O termo a{} da sua PA é: {}'.format(c,d))
print('ACABOU!')

#outra opção:
for c in range (1,11):
    d = a + (c-1)*r
    print(d, end=' -> ')
print('ACABOU!')