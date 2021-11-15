# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('*' * 30)
print('{:^30}'.format('BANCO NATH'))  # irá centralizar o texto dentro da quantidade de caracteres especificados
print('*'*30)

valor = int(input('Qual valor você quer sacar? R$: '))
print('-'*30)
cedula = 50
count_cedula = 0

while True:
    if  valor >= cedula:
        valor = valor - cedula
        count_cedula += 1
    else:
        if count_cedula > 0:
            print('{} cédula(s) de R$ {}.'.format(count_cedula,cedula))
        count_cedula = 0
        cedula = 20
        if valor >= cedula:
            valor -= cedula
            count_cedula +=1
        else:
            if count_cedula > 0:
                print('{} cédula(s) de R$ {}.'.format(count_cedula,cedula))
            count_cedula = 0
            cedula = 10
            if valor >= cedula:
                valor -= cedula
                count_cedula += 1
            else:
                if count_cedula > 0:
                    print('{} cédula(s) de R$ {}.'.format(count_cedula,cedula))
                count_cedula = 0
                cedula = 5
                if valor >= cedula:
                    valor -= cedula
                    count_cedula += 1
                else:
                    if count_cedula > 0:
                        print('{} cédula(s) de R$ {}.'.format(count_cedula,cedula))
                    count_cedula = 0
                    cedula = 1
                    if valor >= cedula:
                        valor -= cedula
                        count_cedula += 1
                    else:
                        if count_cedula > 0:
                            print('{} nota(s) de {}.'.format(count_cedula, cedula))
                        break
print('-'*30)
print('Operação efetuada com sucesso!')

'''
Resolução do Professor Guanabara:

print('=' * 30)
print('{:^30}'.format('BANCO CEV')) 
print('='*30)
valor = int(input('Qual valor você quer sacar? R?$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd >0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
'''
