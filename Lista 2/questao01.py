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
        
