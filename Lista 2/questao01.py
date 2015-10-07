'''
Como resolvi.

LadoA = int(input('Qual a medida do Lado A? '))
LadoB = int(input('Qual a medida do Lado B? '))
LadoC = int(input('Qual a medida do Lado C? '))

if ((LadoA * LadoB) * LadoC) / LadoA**3 == 1:
    print('Triangulo Equilátero')
elif LadoA == LadoB:
    print('Triangulo Isóceles')
elif LadoB == LadoC:
    print('Triangulo Isóceles')
elif LadoA == LadoC:
    print('Triangulo Isóceles')    
else:
    print('Triangulo Escaleno')
        
'''

# Como foi resolvido no video

a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))
if a > b + c or b > a + c or c > a + b:
    print ('Não pode ser um triângulo')
    print ('Um dos lados é maior que a soma dos outros')
elif a == b == c:
    print ('Equilátero')
elif a == b or b == c or a == c:
    print ('Isósceles')
else:
    print ('Escaleno')
