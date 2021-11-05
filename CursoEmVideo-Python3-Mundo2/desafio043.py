# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

print('\33[1:33m-\33[m'*17)  # "-" em cor amarela
print('\33[1:32:40mCALCULADOR DE IMC\33[m') # fundo preto, frase na cor verde
print('\33[1:33m-\33[m'*17) # "-" em cor amarela

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso/(altura**2)
print('Seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está \33[1mAbaixo do Peso\33[m!')
elif imc >= 18.5 and imc <25:
    print('Você está no \33[1:32mPeso Ideal\33[m!')
elif 25 <= imc < 30:
    print('Você está com \33[1:36mSobrepeso\33[m!')
elif imc >= 30 and imc < 40:
    print('Você está \33[1:35mObeso\33[m!')
else:
    print('Você está com \33[1:33mObesidade Mórbida\33[m!')
