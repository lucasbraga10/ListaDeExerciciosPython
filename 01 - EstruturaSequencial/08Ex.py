import datetime
'''08 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.'''

valor_hora = float(input('Digite o valor da hora trabalhada: '))
horas_trabalhadas = float(
  input('Digite apenas a quantidade de horas trabalhadas: '))
minutos_trabalhados = float(
  input('Digite apenas a quantidade de minutos trabalhados: '))
salario = float(
  ((horas_trabalhadas + (minutos_trabalhados / 60)) * valor_hora))

print(f'O salário será de R$:{salario:.2f} reais.')
