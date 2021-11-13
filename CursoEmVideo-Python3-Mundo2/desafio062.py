# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite o a razão da P.A: '))

print("Os 10 primeiros termos da PA são: ", end ='')
contador = 1
pa = primeiro_termo
conta_termos = 0
while contador<=10:
    print(f'{pa}', end=' -> ')
    pa += razao
    contador += 1
    conta_termos += 1
print('Fim?')

mais_termos = 1
nova_pa = pa

while mais_termos != 0:
    mais_termos = int(input('Quer acrescentar mais termos? Quantos? \nR: '))
    novo_contador = 0
    if mais_termos == 0:

        print('FIM! A progressão teve {} termos!'.format(conta_termos))
    else:
        while novo_contador < mais_termos:
            print(f'{nova_pa}', end=' -> ')
            nova_pa += razao
            novo_contador += 1
            conta_termos += 1


