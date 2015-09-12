# -*- coding: cp1252 -*-
cig = int(input('Qtde de cigarros por dia: '))
time = int(input('Qtos anos fumando? '))

total = float((((time * 365) * cig) * 10)/60)/24

print ('Você já perdeu %.2f dias de sua vida fumando!!!' %total)



