'''
Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
divisíveis por 7?
'''

a = 1067
par = 0
for a in list(range(1067, 3627)):
    if a %2 == 0 and a%7==0:
        par += 1
print (par)
