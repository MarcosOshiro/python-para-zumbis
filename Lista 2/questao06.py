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
