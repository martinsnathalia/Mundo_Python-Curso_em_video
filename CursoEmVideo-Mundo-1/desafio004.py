# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo: ')
print('O tipo desse valor é: ',type(n))
print('É apenas numérico?', n.isnumeric()) #is numeric?
print('É alfabético? ',n.isalpha()) #é alfanumérico?
print('Está todo em maiúsculo? ',n.isupper()) #é somente maiúsculo?
print('É somente espaços? ',n.isspace())
print('É alfanumérico ',n.isalnum())
print('Está em minúscula? ',n.islower())
print('Está capitalizada {}'.format(n.istitle()))
