#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

k = float(input('Digite a quantidade de km percorridos: '))
d = int(input('Digite a quantidade de dias que o carro foi alugado: '))

print('O valor a ser pago por {} dias e {} km percorridos é de R$ {:.2f}'.format(d,k,((60*d)+(0.15*k))))
