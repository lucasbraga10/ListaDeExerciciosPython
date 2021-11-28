"""18 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida."""

data = input('Digite uma data: ')
if len(data) == 8:
    dia = int(data[:2])
    mes = int(data[2:4])
    ano = int(data[4:])
    valida = False


    # MES DE 31 DIAS
    if mes in (1, 3, 5, 7, 8, 10, 12):
        if dia < 31:
            valida = True

    # MES DE 30 DIAS
    elif mes in (4, 6, 9, 11):
        if dia < 30:
            valida = True

    elif mes == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            if dia < 29:
                valida = True
            elif dia < 28:
                valida = True

    if valida:
        print('Data valida')
    else:
        print('Data inválida')
else:
    print('Data invalida')