pre = input('Entre com o preço: ')
desc = input('Informe a % de desconto: ')

desconto = int(pre) * (float(desc)/100)
new_pre = int(pre) - desconto

print('O desconto é de R$%.2f ' %desconto)
print('O novo preço fica em R$%.2f ' %new_pre)
