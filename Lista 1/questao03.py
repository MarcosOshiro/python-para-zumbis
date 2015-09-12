dia = input('Qtos dias? ')
hora = input('Qtas horas? ')
minuto = input('Qtos minutos? ')
segundo = input('Qtos segundos? ')


c_dia = ((int(dia) * 24) * 60) * 60
c_hora = ((int(hora) * 60) * 60)
c_minuto = (int(minuto) * 60)

#print(c_dia)
#print(c_hora)
#print(c_minuto)


total = c_dia + c_hora + c_minuto + int(segundo)

print ('São %d segundos no total!!!' %total)
