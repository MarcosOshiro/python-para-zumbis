'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas.
Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento
efetuado desprezando os centavos.  Suponha que as notas para troco sejam as de
50, 20, 10, 5, 2 e 1 reais, e que nenhuma delas esteja em falta no caixa.
'''

'''Primeira tentativa

conta = float(input("Entre com o total da conta: "))
pagamento = float(input("Entre com o pagamento: "))
troco = pagamento - conta
n50 = 0 
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0
sum_notas = n50 + n20 + n10 + n5 + n2 + n1
calc = troco

while calc <= troco:
    if calc <= 1.0:
        break
    elif calc >= 50.0:
        calc = calc - 50.0
        n50 += 1
    elif calc < 50.0:
        if calc <= 1.0:
            break
        elif calc >= 20.0:
            calc = calc - 20.0
            n20 += 1
        elif calc < 20.0:
            if calc <= 1.0:
                break
            elif calc >= 10.0:
                calc = calc - 10.0
                n10 += 1
            elif calc < 10.0:
                if calc <= 1.0:
                    break
                elif calc >= 5.0:
                    calc = calc - 5.0
                    n5 += 1
                elif calc < 5.0:
                    if calc <= 1.0:
                        break
                    elif calc >= 2.0:
                        calc = calc - 2.0
                        n2 += 1
                    elif calc < 2.0:
                        if calc <= 1.0:
                            break
                        elif calc >= 1.0:
                            calc = calc - 1.0
                            n1 += 1
                        elif calc < 1.0:
                            if calc <= 1.0:
                                break
print("Foram usadas %d notas" %sum_notas)
print("Qtde de R$50,00: %d" %n50)            
print("Qtde de R$20,00: %d" %n20)
print("Qtde de R$10,00: %d" %n10)
print("Qtde de R$5,00: %d" %n5)
print("Qtde de R$2,00: %d" %n2)
print("Qtde de R$1,00: %d" %n1)
'''

conta = int(input("Digite o valor total da compra: "))
pagamento = int(input("Digite a quantia de dinheiro recebida: "))


troco = pagamento-conta
notas = [100, 50, 20, 10, 5, 2, 1]

if troco > 0:
    print ("Valor do troco: R$ %s." %troco)
    for p in notas:
        if troco >= p:
            n = int(troco/p)
            r = troco - p*n
            print (" %s nota(s) de R$ %s." %(n, p))
            troco = r
else:
    print ("Pagamento insuficiente.")
    
        







