'''11 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 * o produto do dobro do primeiro com metade do segundo .
 * a soma do triplo do primeiro com o terceiro.
 * o terceiro elevado ao cubo.'''

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = float(input('Digite um número real: '))

print(f'O produto do dobro do primeiro com metade do segundo é igual a {(n1*2) * (n2/2)}')
print(f'A soma do triplo do primeiro com o terceiro é igual a {(n1*3) + n3}')
print(f'O terceiro elevado ao cubo é igual a {n3**3}')
