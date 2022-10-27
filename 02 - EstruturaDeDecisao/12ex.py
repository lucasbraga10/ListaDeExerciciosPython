'''12 - Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

# ENTRADA DE DADOS
valor_hora = float(input('Digite o valor da hora trabalhada: '))
hora_trabalhada = float(input('Digite a quantidade de horas trabalhadas: '))

# VARIAVEIS
salario_bruto = valor_hora * hora_trabalhada
ir = 0
irp = 0
inss = salario_bruto * (10 / 100)
fgts = salario_bruto * (11 / 100)
sindicato = salario_bruto * (3 / 100)
total_desconto = ir + inss + sindicato

# LÓGICA
if salario_bruto <= 900:
  ir = 0
  irp = str('ISENTO')

if salario_bruto > 900:
  if salario_bruto <= 1500:
    ir = salario_bruto * (5 / 100)
    irp = str('5%')

if salario_bruto > 1500:
  if salario_bruto <= 2500:
    ir = salario_bruto * (10 / 100)
    irp = str('10%')

if salario_bruto > 2500:
  ir = salario_bruto * (20 / 100)
  irp = str('20%')

print(f''' 
Salário Bruto: R$ {salario_bruto}
(-) IR ({irp}): R$  {ir}
(-) INSS (10%): R$ {inss}
(-) SINDICATO (3%): R$: {sindicato}
FGTS (11%): R$ {fgts}
Total de descontos: R$ {total_desconto}
Salário Liquido: R$ {salario_bruto - total_desconto} 
''')
