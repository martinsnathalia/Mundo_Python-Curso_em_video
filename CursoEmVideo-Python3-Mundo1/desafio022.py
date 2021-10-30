# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip() # strip remove os espaços do início e do final da frase
print('Todas as letras maiúsculas: ',nome.upper())
print('Todas as letras minúsculas: ', nome.lower())

a = nome.count(' ')
b = len(nome)
c = b - a
print('O seu nome todo tem {} letras'.format(c))

d = nome.split() # irá separar as palavras em uma lista
e = d[0] # selecionará a primeira palavra da lista
print('O primeiro nome tem {} letras'.format(len(e)))

#print('O primeiro nome tem {} letras'.format(nome.find(' ')))
# nome.find(' ') encontrará o primeiro espaço, e portanto, será após o primeiro nome, mostrando o tamanho dele



