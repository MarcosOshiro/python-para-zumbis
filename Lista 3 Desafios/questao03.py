'''
Verifique se um inteiro positivo n é primo.
'''

n = int(input("Entre com um número inteiro positivo: "))

if n%2 == 0:
    print("Não é primo")
elif n%3 == 0:
    print("Não é primo")
else:
    print("Número primo")

'''
Como foi resolvido no video

n = int(input('Número: '))
k = 1
divisores = 0
while k <= n:
    if n % k == 0:
        divisores = divisores + 1
    k = k + 1
print(divisores == 2)
'''

