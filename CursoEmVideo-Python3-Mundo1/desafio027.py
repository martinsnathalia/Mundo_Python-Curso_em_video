# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()
lista_nome = nome.split()
tamanho_lista = len(lista_nome)
print('O primeiro nome será: {}'.format(lista_nome[0]))
print('O último nome será: {}'.format(lista_nome[tamanho_lista-1]))
