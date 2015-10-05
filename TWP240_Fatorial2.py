'''
Fiz assim:

n = int(input('Informe o número: '))
fat = 1
while n >= 1:
    fat = fat * n
    n = n - 1

print ('fatorial: %5.2f' %fat)
'''

i = 1
fat = 1
n = int(input("Digite n: "))
while i <=n:
    fat = fat * i
    i = i + 1
print ("Fat (%d) = %d" %(n, fat))
