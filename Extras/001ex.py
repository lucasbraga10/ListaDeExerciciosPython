numero = input('Digite um número inteiro: ')

try:
  numero = int(numero)
  if numero % 2 == 0:
    print('O número digitato é um número PAR')
  else:
    print('O número digitado é um número IMPAR')
except:
  print('Voce não digitou um número inteiro')
