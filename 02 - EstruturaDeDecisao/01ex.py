'''01 - Faça um Programa que peça dois números e imprima o maior deles.'''

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
maior = 0

if n1 > n2:
    maior = n1
else:
    maior = n2

print(f'O maior número digitado foi o {maior}')
