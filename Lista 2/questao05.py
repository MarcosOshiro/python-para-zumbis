'''
Como fiz

n1=int(input('1º número: '))
n2=int(input('2º número: '))
n3=int(input('3º número: '))

if n1 > n2:
    if n1 > n3:
        print('O maior número é %d' %n1)
    else:
        print('O maior número é %d' %n3)
elif n2 > n3:
    print('O maior número é %d' %n2)
else:
    print('O maior número é %d' %n3)

if n1 < n2:
    if n1 < n3:
        print('O menor número é %d' %n1)
    else:
        print('O menor número é %d' %n3)
elif n2 < n3:
    print('O menor número é %d' %n2)
else:
    print('O menor número é %d' %n3)
    
'''

#Como foi feito no video

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a >= b and a >= c:
    print ('Maior: %d' %a)
elif b >= c:
    print ('Maior: %d' %b)
else:
    print ('Maior: %d' %c)

if a <= b and a <= c:
    print ('Maior: %d' %a)
elif b <= c:
    print ('Maior: %d' %b)
else:
    print ('Maior: %d' %c)
