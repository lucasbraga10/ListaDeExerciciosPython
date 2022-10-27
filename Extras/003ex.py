nome = input('Digite o seu primeiro nome: ').strip().lower()

if len(nome) <= 4:
  print('Seu nome é curto')
elif 5 <= len(nome) <= 6:
  print('Seu nome é normal')
elif len(nome) >= 7:
  print('Seu nome é muito longo')
