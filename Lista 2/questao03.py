peso = int(input('Qual o total de peso dos peixes?(Kg) '))
excesso = 0
multa = 0

if peso > 50:
    excesso = int(peso - 50)
    multa = int(excesso*4)
else:
    excesso = int(0)
    multa = int(0)

print('Você ultrapassou %.2f Kg, e deve pagar R$ %.2f de multa'%(excesso,multa))
