# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input('Digite uma frase, sem acento, para saber se é um palíndromo: ')).strip().upper() #corta o espaço no início e fim, torna maiúscula
palavras = frase.split() #cortará os espaços
junto = ''.join(palavras) #vai concatenar as palavras sem espaço
inverso = '' #deixará nenhum espaço

for c in range (len(junto)-1,-1,-1):
    inverso = inverso + junto[c] #irá juntar as palavras, sem nenhum espaço, de trás para frente

'''#poderia utilizar também o fatiamento, sem necessidade do for:
inverso = junto[::-1]'''

print('O inverso de {} é {}.'.format(junto,inverso))
if inverso == junto:
    print('Essa palavra é um palíndromo!')
else:
    print('Essa palavra não é um palíndromo!')


