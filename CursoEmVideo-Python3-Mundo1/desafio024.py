# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Digite o nome de uma cidade: '))
maiusc = cidade.upper()
listacidade = maiusc.split()
primeiro_termo = listacidade[0]
resultado = primeiro_termo.find('SANTO')
print('Se retornar 0: a cidade começa com Santo;\nSe retornar -1: não começa com Santo. \nResultado: {}'.format(resultado))
# outra forma:
resultado_2 = "SANTO" in primeiro_termo
print('A cidade começa com a palavra Santo:',resultado_2)

# outra forma:
#cid = str(input('Digite o nome de uma cidade: ')).strip()  #usa-se o strip para retirar os espaços
#print(cid[:5].upper() == 'SANTO') # Santo possui 5 letras, na str vai de 0 a 4. Logo, esse programa irá analisar as 5 letras.



