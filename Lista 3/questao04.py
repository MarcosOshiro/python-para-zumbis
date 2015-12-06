'''
A sequencia de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
Sua regra de formação é simples: os dois primeiros elementos são 1; a partir
de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que
leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1,
F3 = 2, etc.
'''
'''
def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
print (fib(6))


Copiei descaradamente, não consegui aplicar conhecimento aqui. Preocupante.
Abaixo só consegui pq entendi o que o maluco de cima fez... too sad ):
'''

n = int(input("Número: "))
a = 1
b = 1
x = 1
while x <= (n-1): #n-1 pq começa do zero
    a,b = b, a+b
    x += 1

print (a)

'''
Como resolveu em video

n = int(input('N: '))
a, b = 1, 1
k = 1

while k <= n -x:
    a, b = b, a + b
    k = k + 1

print('Fib (%d) = %d' %(n, b))
'''
