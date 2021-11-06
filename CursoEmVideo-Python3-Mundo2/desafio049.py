# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input('Digite um número para saber sua tabuada: '))

for c in range(1,11):
    t = tabuada*c
    print('{} x {:2} = {}'.format(tabuada,c,t))
