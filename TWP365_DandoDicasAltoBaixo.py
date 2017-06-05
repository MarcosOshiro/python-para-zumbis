print ("Bem Vindo ao jogo da adivinhação")
n = input("Digite um número: ")
chute = int(n)
while chute != 42:
    if chute > 42:
        print("Não foi dessa vez! chutou bem ALTO!")
        n2 = input("Digite outro número: ")
        chute = int(n2)
    else:
        print("Não foi dessa vez! chutou bem BAIXO!")
        n2 = input("Digite outro número: ")
        chute = int(n2)
print("Uau!! Na mosca! Vc acertou!!!")


""" Como foi feito no video
print ('Bem Vindo!')
chute = 0
while chute != 42:
    g = input ('Chute um número: ')
    chute = int(g)
    if chute == 42:
        print ('Você venceu!')
    else:
        if chute > 42:
            print ('Alto')
        else:
            print ('Baixo')
print ('Fim de jogo!')
