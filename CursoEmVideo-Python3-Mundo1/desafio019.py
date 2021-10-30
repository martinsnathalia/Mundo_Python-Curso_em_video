# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
a = input("Digite o nome do primeiro aluno: ")
b = input("Digite o nome do segundo aluno: ")
c = input("Digite o nome do terceiro aluno: ")
d = input("Digite o nome do quarto aluno: ")
#lista = [a,b,c,d]
#print('O aluno que deverá apagar o quadro é {}'.format(random.choice(lista)))
print('O aluno que deverá apagar o quadro é {}'.format(random.choice([a,b,c,d])))

#choice serve para escolher entre um dos números

