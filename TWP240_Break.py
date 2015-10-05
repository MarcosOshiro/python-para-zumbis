'''
Fiz dessa forma

n = 1
soma = 0
x = 1
while n != 0:
    if x == 0:
        break
    else:
        x = int(input('Digite o %d núnero: ' %n))
        soma = soma + x
        n = n + 1

print ('Soma: %d' %soma)
'''

soma = 0
while True:
    x = int(input('Digite o número (0 sai): '))
    if x == 0:
        break
    soma = soma + x
print ("Soma: %d" %soma)
