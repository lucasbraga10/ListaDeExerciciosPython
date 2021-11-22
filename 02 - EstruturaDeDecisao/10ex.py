'''01 - Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou
V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",
conforme o caso.'''

turno = str(input('O seu turno é? M-matutino ou V-Vespertino ou N- Noturno? ')).strip().lower()

if turno[0] == 'm':
    print('Bom Dia!')

if turno[0] == 'v':
    print('Boa Tarde!')

if turno[0] == 'n':
    print('Boa Noite!')

if turno[0] not in 'mvn':
    print('Valor Inválido!')
