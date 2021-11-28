"""16 - Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá
pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""
from math import sqrt
a = float(input('Digite o valor de A:'))
if a != 0:
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
    delta = b**2 - (4 * a * c)
    if delta < 0:
        print('\nO delta calculado é negativo, a equação não possui raizes reais')
        print(f'Delta = {delta}')
    elif delta == 0:
        raiz = (-b + (sqrt(delta))) / (2*a)
        print('\bO delta calculado é igual a zero a equação possui apenas uma raiz real')
        print(f'Delta = {delta}')
        print(f'Raiz de delta = {raiz}')
    else:
        x1 = (-b + (sqrt(delta))) / (2*a)
        x2 = (-b - (sqrt(delta))) / (2*a)
        print('\nO delta calculado é positivo, a equação possui duas raiz reais')
        print(f'Delta = {delta}')
        print(f'X1 = {x1}')
        print(f'X2 = {x2}')

else:
    print('\nSe A = 0, a equação não é do segundo grau.')
    print('Programa encerrado')

