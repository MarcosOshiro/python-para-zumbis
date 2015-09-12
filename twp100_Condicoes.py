vel = int(input('Qual a velocidade? '))

if vel > 110:
    multa = (vel - 110) * 5.00
    print ('Você foi multado em R$%.2f!' %multa)
else:
    print ('Tudo bem!!!')
