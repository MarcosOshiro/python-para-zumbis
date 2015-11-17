'''
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que
o usuário informe um valor válido.
'''

nota = int(input("Entre com a nota (0 a 10): "))
while nota < 0 or nota > 10:
        nota = int(input("Nota inválida, digite uma nota entre zero e dez: "))
print ("Valor válido!")
