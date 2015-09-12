fatura = int(input('Quantos minutos foram gastos? '))

if fatura < 200:
    totfatura = fatura * 0.20
    print ('Você deve pagar R$ %.2f ' %totfatura)
elif fatura >= 200 and fatura <= 400:
    totfatura = fatura * 0.18
    print ('Você deve pagar R$ %.2f ' %totfatura)
else:
    totfatura = fatura * 0.15
    print ('Você deve pagar R$ %.2f ' %totfatura)
