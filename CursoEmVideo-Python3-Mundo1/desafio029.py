# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Digite a velocidade do seu carro em km/h: '))

if v > 80:
    print('O limite é de 80 km/h. Você será multado no valor de R$ {:.2f}'.format((v-80)*7))
else:
    print('Tirou onda! Tá no limite.')
print('Tenha um bom dia!')

#condição simples é quando não há o else.
