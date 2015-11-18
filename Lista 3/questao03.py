'''
Supondo que apopulação de um páis A seja da ordem de 80.000 habitantes com uma
taxa anual de crescimento de 3.0% e que a população de B seja 200.000 habitantes
com uma taxa de crescimento de 1.5%.  Faça um programa que calcule e escreva
o número de anos necessários para que a população do país A ultrapasse ou iguale
a população do país B, mantidas as taxas de cresscimento.
'''

A = 80000
B = 200000
txA = 0.03
txB = 0.015
anos = 0

while A < B:
    anos += 1
    A = A + (A*txA)
    B = B + (B*txB)

print("A cidade A irá demorar %d anos para chegar na cidade B" %anos)


