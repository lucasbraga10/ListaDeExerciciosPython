'''07 - Faça um Programa que leia três números e mostre o maior e o menor deles.'''

n1 = float(input('Digite o primeito número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
menor = n1
maior = n1

if n2 < n1 and n2 < n3:
  menor = n2

elif n3 < n1 and n3 < n2:
  menor = n3

if n2 > n1 and n2 > n3:
  maior = n2

elif n3 > n1 and n3 > n2:
  maior = n3

print(f'O menor número digitado foi o {menor}')
print(f'O maior número digitado foi o {maior}')
