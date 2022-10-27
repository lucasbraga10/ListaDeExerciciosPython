'''10 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.'''

cel = float(input('Digite a temperatura em Celsius: '))
fah = (cel * (9 / 5)) + 32

print(f'A temperatura em graus Fahrenheit é de {fah:.1f}')
