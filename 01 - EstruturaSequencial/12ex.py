'''12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58'''

altura = float(input('Digite sua altura em metros: '))
imc = float(72.7 * altura) - 58

print(f'O seu peso ideal é de {imc:.2f}')
