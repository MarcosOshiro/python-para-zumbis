'''
Como resolvi

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

'''

#Como foi feito no video

a = int(input('Ano: '))
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print ('Bissexto')
else:
    print ('Não é bissexto')
