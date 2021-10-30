# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

name = str(input('Digite o seu nome: ')).strip()
verify_silva = "SILVA" in name.upper()
print('Você possui Silva no nome: ',verify_silva)
