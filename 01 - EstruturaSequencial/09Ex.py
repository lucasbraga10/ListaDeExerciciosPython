'''09 - Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius'''

fah = float(input('Digite a temperatura em Fahrenheit: '))
ce = 5 * ((fah-32) / 9)

print()
print(f'A temperatura em graus Celsius é de {ce:.2f}')
