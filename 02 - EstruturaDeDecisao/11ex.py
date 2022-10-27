'''11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no
salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.'''

salario_atual = float(input('Digite o salário atual: '))
percentual_aumento = int
valor_aumento = float
salario_novo = float

if salario_atual <= 280:
  percentual_aumento = 20
  valor_aumento = salario_atual * (percentual_aumento / 100)
  salario_novo = salario_atual + (salario_atual * (percentual_aumento / 100))

if salario_atual > 280:
  if salario_atual <= 700:
    percentual_aumento = 15
    valor_aumento = salario_atual * (percentual_aumento / 100)
    salario_novo = salario_atual + (salario_atual * (percentual_aumento / 100))

if salario_atual > 700:
  if salario_atual <= 1500:
    percentual_aumento = 10
    valor_aumento = salario_atual * (percentual_aumento / 100)
    salario_novo = salario_atual + (salario_atual * (percentual_aumento / 100))

if salario_atual > 1500:
  percentual_aumento = 5
  valor_aumento = salario_atual * (percentual_aumento / 100)
  salario_novo = salario_atual + (salario_atual * (percentual_aumento / 100))

print(f'''
Salario Atual: {salario_atual}
Percentual de Aumento: {percentual_aumento}
Valor de Aumento: {valor_aumento:.2f}
Novo Salário, Após o Aumento: {salario_novo}
''')
