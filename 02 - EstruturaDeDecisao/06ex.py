'''06 - Faça um Programa que leia três números e mostre o maior deles.'''

n1 = float(input('Digite o primeito número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 > n2 > n3:
    print(f'O maior número digitado foi o {n1}')
elif n2 > n1 >n3:
    print(f'O maior número digitado foi o {n2}')
else:
    print(f'O maior número digitado foi o {n3}')
