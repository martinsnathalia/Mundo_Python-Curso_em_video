# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

t = float(input('Digite a temperatura em °C: '))
print('A temperatura {}ºC equivale a {}°F'.format(t,((( 9 / 5 ) * t) + 32)))

