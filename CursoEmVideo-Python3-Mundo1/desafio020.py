# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
# from random import shuffle

a = input("Digite o nome do primeiro aluno: ")
b = input("Digite o nome do segundo aluno: ")
c = input("Digite o nome do terceiro aluno: ")
d = input("Digite o nome do quarto aluno: ")
lista = [a,b,c,d]
random.shuffle(lista)
#shuffle(lista)

print('A ordem a ser sorteada para apresentação do trabalho é : ', lista)
#print('A ordem a ser sorteada para apresentação do trabalho é : {}'.format(random.sample([a,b,c,d],k=4)))

#sample serve para sortear os números sem repetição


