# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Digite o valor em metros: '))
print('Esse valor em decímetro é {:.0f} dm'.format(n*10))
print('Esse valor em centímetros é {:.0f} cm'.format(n*100))
print('Esse valor em milímetros é {:.0f} mm'.format(n*1000))
print('Esse valor em decâmetro é {} dam'.format(n*0.1))
print('Esse valor em hectômetro é {} hm'.format(n*0.01))
print('Esse valor em kilômetro é {} km'.format(n*0.001))