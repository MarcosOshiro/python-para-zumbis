# -*- coding: cp1252 -*-
qtdkm = int(input('Qual a qtde de km percorrido? '))
qtddia = int(input('Informe qtde de dias de aluguel? '))

valkm = qtdkm * 0.15
valdia = qtddia * 60.00
total = valkm + valdia
print ('O total é de R$%.2f' %total)
