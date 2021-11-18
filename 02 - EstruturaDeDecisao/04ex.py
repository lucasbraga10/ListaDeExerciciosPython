'''04 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input('Digite ume letra: ').lower()

if letra in ('a', 'e', 'i', 'o', 'u'):
    print('Voce digitou uma vogal.')
else:
    print('Voce digitou uma consoante')
