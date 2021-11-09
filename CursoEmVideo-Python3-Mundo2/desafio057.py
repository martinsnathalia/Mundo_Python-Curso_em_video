# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = str(input('Digite qual é o seu gênero: ')).upper().strip() #pega somente a primeira letra
while s!='M' and s!='F' and s!='NB':
#while s not in 'MmFfNBnb': - outra opção para uso do While
    s = str(input('Dados inválidos. Digite novamente seu gênero: ')).upper().strip()
print('Gênero {} registrado com sucesso.'.format(s))
if s=='F':
    print('VocÊ é mulher!')
if s=='M':
    print('VocÊ é homem!')
if s=='NB':
    print('VocÊ é NB!')


