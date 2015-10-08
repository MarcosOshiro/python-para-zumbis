notas = [2,3,4,5,6]
x = 0
soma = 0
while x <= 4:
    soma = soma + float(notas[x])
    x = x + 1
media = soma / 5
print ('Sua média é: %.2f' %media) 

'''
Como foi resolvido no video

notas = [6, 7, 5, 8, 9]
soma = 0
x = 0
while x < 5:
    soma += notas [x]
    x += 1
print ("Média: %5.2f" %(soma/x))

Obs.: X += 1 é o mesmo que x = x + 1
'''
