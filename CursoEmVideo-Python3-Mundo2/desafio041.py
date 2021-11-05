# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
from time import sleep
print('#'*38)
print('\33[1:36mDescubra a que categoria você pertence!\33[m')
print('#'*38)
sleep(1)
ano = int(input('Digite o ano do seu nascimento: '))

atual = date.today().year

idade = atual - ano
print('O atleta tem {} anos!'.format(idade))

if idade <= 9:
    print('Sua categoria é \33[1:33mMIRIM\33[m!')
elif idade <= 14:
    print('Sua categoria é \33[1:31mINFANTIL\33[m!')
elif idade <= 19:
    print('Sua categoria é \33[1:35mJUNIOR\33[m!')
elif idade <= 20:
    print('Sua categoria é \33[1:34mSÊNIOR\33[m!')
else:
    print('Sua cateogria é \33[1:32mMASTER\33[m!')