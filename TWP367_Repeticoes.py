from random import randint
print ("Bem Vindo ao jogo da adivinhação")
n = input("Digite um número: ")
chute = int(n)
sorteio = randint(1,100)
while chute != sorteio:
    if chute > sorteio:
        print("Não foi dessa vez! chutou bem ALTO!")
        n2 = input("Digite outro número: ")
        chute = int(n2)
    else:
        print("Não foi dessa vez! chutou bem BAIXO!")
        n2 = input("Digite outro número: ")
        chute = int(n2)
print("Uau!! Na mosca! Vc acertou!!!")

