# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('\33[1:34m*\33[m'*31) # "*" na cor azul
print('\33[1:32mQUAL É O SEU TIPO DE TRIÂNGULO?\33[m') # frase na cor verde
print('\33[1:34m*\33[m'*31) # "*" na cor azul

l1 = float(input('Digite o tamanho do primeiro lado do triângulo: '))
l2 = float(input('Digite o tamanho do segundo lado: '))
l3 = float(input('Agora digite o do terceiro lado: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    if l1 == l2 == l3:
        print('Esses lados formam um triângulo \33[1:36mEQUILÁTERO\33[m!')
    elif l1 != l2 != l3 != l1:
        print('Esses lados formam um triângulo \33[1:35mESCALENO\33[m')
    else:
        print('Esses lados formam um triângulo \33[1:31mISÓSCELES\33[m!')
else:
    print('Esses lados \33[1:34mNÃO\33[m formam um triângulo!')