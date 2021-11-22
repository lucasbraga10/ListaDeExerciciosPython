'''09 - Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

if n1 < n3:
    n1, n3 = n3, n1

if n1 < n2:
    n1, n2 = n2, n1

if n2 < n3:
    n2, n3 = n3, n2

print(f'Os números ordenados ficam {n1}, {n2}, {n3}')