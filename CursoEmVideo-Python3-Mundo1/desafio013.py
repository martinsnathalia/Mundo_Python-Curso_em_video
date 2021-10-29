# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o seu salário em reais: '))
print('O valor do seu salário com 15% de aumento será {:.2f} reais'.format(salario + (salario * 0.15)))
