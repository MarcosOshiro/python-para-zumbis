ano = int(input('Digite o ano que deve ser testado: '))

if ano%4==0:
    if ano%100==0:
        if ano%400==0:
            print('Ano bissexto')
        else:
            print('Ano não bissexto')
    else:
        print('Ano não bissexto')

else:
    print('Ano não bissexto')
