"""14 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o
conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E."""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

print()
if media >= 9:
  print(f'Primeira nota: {nota1}')
  print(f'Segunda nota: {nota2}')
  print(f'Média: {media}')
  print('Nota Final: A')
  print('APROVADO')

if media >= 7.50:
  if media < 9:
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Média: {media}')
    print('Nota Final: B')
    print('APROVADO')

if media >= 6:
  if media < 7.50:
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Média: {media}')
    print('Nota Final: C')
    print('APROVADO')

if media >= 4:
  if media < 6:
    print(f'Primeira nota: {nota1}')
    print(f'Segunda nota: {nota2}')
    print(f'Média: {media}')
    print('Nota Final: D')
    print('REPROVADO')

if media < 4:
  print(f'Primeira nota: {nota1}')
  print(f'Segunda nota: {nota2}')
  print(f'Média: {media}')
  print('Nota Final: E')
  print('REPROVADO')
