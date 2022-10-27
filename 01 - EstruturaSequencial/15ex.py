'''15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
 total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
 para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.'''

valor_hora = float(input('Digite o valor do salário por hora: '))
horas_trabalhadas = float(input('Digite apenas os HORAS TRABALHADAS: '))
minutos_trabalhados = float(input('Digite apenas os MINUTOS TRABALHADOS: '))
salario_bruto = float((horas_trabalhadas * valor_hora) +
                      ((minutos_trabalhados / 60) * valor_hora))
ir = salario_bruto * (11 / 100)
inss = salario_bruto * (8 / 100)
sindi = salario_bruto * (5 / 100)

print(f'''
+ Salário Bruto: R${salario_bruto:.2f}
- IR (11%): R${ir:.2f}
- INSS (8%): R${inss:.2f}
- Sindicato ( 5%): R${sindi:.2f}
= Salário Liquido: R${salario_bruto - ir - inss - sindi:.2f}
''')
