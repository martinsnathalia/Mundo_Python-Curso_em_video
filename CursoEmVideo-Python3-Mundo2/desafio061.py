# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

a = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite o a razão da P.A: '))

contador = 1

while contador < 11:
    pa = a + (contador-1)*r
    print('O {}º termo da PA é: {}.'.format(contador,pa))
    contador += 1
print('FIM!')
