sal = input('Entre com o valor do salário: ')
por = input('Informe a % de aumento: ')

aumento = int(sal) * (float(por)/100)
new_sal = int(sal) + aumento

print('O aumento é de R$%.2f ' %aumento)
print('Seu salário fica em R$%.2f ' %new_sal)
