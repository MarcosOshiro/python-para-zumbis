'''
Como fiz

valorhora=(input('Quanto você ganha por hora? '))
qtdehora=(input('Quantas horas você trabalhou no mês? '))

sal_bruto = float(valorhora) * float(qtdehora)
ir = float(sal_bruto) * 0.11
inss = float(sal_bruto) * 0.08
sindicato = float(sal_bruto) * 0.05
sal_liquido = (((float(sal_bruto) - ir)-inss)-sindicato)

print('O salario bruto é de: %.2f' %sal_bruto)
print('O desconto de IR é de: %.2f' %ir)
print('O desconto de INSS é de: %.2f' %inss)
print('O desconto do sindicaro é de: %.2f' %sindicato)
print('O salario liquido é de: %.2f' %sal_liquido)
'''

#Como foi feito no video

valor = float(input('Valor por hora: '))
horas = int(input('Horas trabalhadas: '))
bruto = valor * horas
ir = bruto * 0.11
inss = bruto * 0.09
sind = bruto * 0.05
liquido = bruto - ir -inss - sind
print ('+Salário Bruto:\t\t R$ %10.2f' %bruto)
print ('-IR:\t\t\t R$ %10.2f' %ir)
print ('-INSS:\t\t\t R$ %10.2f' %inss)
print ('-Sindicato:\t\t R$ %10.2f' %sind)
print ('=Salário Líquido:\t R$ %10.2f' %liquido)
