hora = input('Digite a hora atual: ')

try:
    hora = int(hora)
    if 0 <= hora <= 11:
        print('Bom Dia')
    elif 12 <= hora <= 17:
        print('Boa Tarde')
    elif 18 <= hora <= 23:
        print('Boa Noite')
    else:
        print('Valor Inválido')

except:
    print('Valor Inválido')
