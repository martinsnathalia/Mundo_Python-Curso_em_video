# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai
# se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu
# programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
idade = int(input('Olá! Informe o seu ano de nascimento: '))

ano = date.today().year
falta = ano-idade
passou = falta - 18

if falta < 18:
    print('Como você possui {} anos, ainda falta(m) {} ano(s) para se alistar!'.format(falta,abs(passou)))
    print('Seu alistamento será em {}'.format(ano+abs(passou)))
elif falta == 18:
    print('Está na hora de você se alistar!')
else:
    print('Já passou {} ano(s) do tempo de se alistar!'.format(abs(passou)))
    print('Você deveria ter se alistado em {}!'.format(ano-abs(passou)))