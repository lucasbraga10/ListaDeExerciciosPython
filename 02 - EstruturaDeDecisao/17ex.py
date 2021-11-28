"""17 - Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano
é ou não bissexto."""



while True:
    data = int(input('Digite o ano a ser verificado (Digite 0 para parar o programa): '))
    if data == 0:
        print('Programa encerrado')
        break
    if data % 4 == 0:
        if data % 100 != 0:
            print('É bissexto')

        elif data % 400 == 0:
            print('É bissexto')

        else:
            print('Não é bissexto')
    else:
        print('Não é bissexto')


