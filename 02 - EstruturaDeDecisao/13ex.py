'''13 - Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.'''

numero = int(
  input('Digite um número entre 1 e 7 para saber o dia da semana: '))

if numero == 1:
  print('Domingo')
elif numero == 2:
  print('Segunda')
elif numero == 3:
  print('Terça')
elif numero == 4:
  print('Quarta')
elif numero == 5:
  print('Quinta')
elif numero == 6:
  print('Sexta')
elif numero == 7:
  print('Sábado')
else:
  print('Valor Inválido')
