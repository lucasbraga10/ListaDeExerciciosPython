'''02 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

n1 = float(input('Digite um número: '))
comparador = float

if n1 > 0:
    print('O número digitado é um número positivo.')

elif n1 == 0:
    print('O número zero é um número considerado neutro.')

else:
    print('O número digitado é um número negativo.')
