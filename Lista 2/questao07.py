'''
Minha solução errada

metros2=input('Informe a área a ser pintada em m²: ')

if int(metros2) < 54:
    print('Você precisa de 1 lata de tinta e gastará R$80,00')
else:
    lata = (int(metros2)/3)/18
    total = int(lata) * 80
    print('Você precisa de %d lata de tinta e gastará R$%.2f' %(lata, total))

'''

# Como foi resolvido no video

m = int(input('Metros: '))
if m % 54 != 0:
    latas = int(m / 54) + 1
else:
    latas = m / 54

valor = latas * 80

print ('%d lata(s) a um custo de %.2f' %(latas, valor))
