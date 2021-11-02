# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Digite o seu salário para saber o seu aumento: '))

if s > 1250:
    print('Seu novo salário será R$ {:.2f}'.format(s * 1.10))
else:
    print('Seu novo salário será R$ {:.2f}'.format(s * 1.15))
