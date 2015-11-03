import random, os, sys
 
tabuleiro = ['', '', '', '', '', '', '', '', '']
jogador_1 = input('Nome do Primeiro jogador: ')
jogador_2 = input('Nome do Segundo jogador: ')
joga = random.randint(1,2)
gameover = 0
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
   
def fim(jogador, opcode):
    clear()
    if opcode == 1:
        print('''
Jogo Atual
{0}_|_{1}_|_{2}
{3}_|_{4}_|_{5}
{6} | {7} | {8}
           FIM DE JOGO
       ---------------------
       Ganhador: {jogador}'''.format(*tabuleiro, jogador =  jogador))
    else:
        print('''
Jogo Atual
{0}_|_{1}_|_{2}
{3}_|_{4}_|_{5}
{6} | {7} | {8}
            FIM DE JOGO
       ---------------------
             GAME OVER ''' .format(*tabuleiro))
        sys.exit(0)
       
def Teste_ganhador(jogador, numero):
    global gameover
    # x0 inicio - Teste diagonal
    if ((numero in tabuleiro[0]) and (numero in tabuleiro[4]) and (numero in tabuleiro[8])) or ((numero in tabuleiro[2]) and (numero in tabuleiro[4]) and (numero in tabuleiro[6])):
        fim(jogador, 1)
    # x0 fim
    #x1 inicio - Teste Horizontal
   
    elif ((numero in tabuleiro[0]) and (numero in tabuleiro[1]) and (numero in tabuleiro[2])) or ((numero in tabuleiro[3]) and (numero in tabuleiro[4]) and (numero in tabuleiro[5])) or ((numero in tabuleiro[6]) and (numero in tabuleiro[7]) and (numero in tabuleiro[8])):
        fim(jogador, 1)
     #x1 fim
 
    #x2 inicio - Teste Vertical
    elif ((numero in tabuleiro[0]) and (numero in tabuleiro[3]) and (numero in tabuleiro[6])) or ((numero in tabuleiro[1]) and (numero in tabuleiro[4]) and (numero in tabuleiro[7])) or ((numero in tabuleiro[2]) and (numero in tabuleiro[5]) and (numero in tabuleiro[8])):
        fim(jogador, 1)
    else:
        for x in tabuleiro:
                if x == "x" or x == "O":
                        gameover += 1
        if gameover == 9:
                fim('', 0)
        else:
                gameover = 0
        clear()
        jogo()
 
def jogo():
    global joga
    if joga == 1:
        play = int(input('''
Jogador = {nome}
Macador = X
Referência:
   0_|_1_|_2
   3_|_4_|_5
   6 | 7 | 8
 
--------------------------------
Jogo Atual
{0}_|_{1}_|_{2}
{3}_|_{4}_|_{5}
{6} | {7} | {8}
Digite a Coordenada da sua jogada: ''' .format(*tabuleiro, nome = jogador_1)))
        if play < 0 or play >9:
                clear()
                prin('Opção Inválida!')
                jogo()
        else:
            if not tabuleiro[play]:
                tabuleiro[play] = 'x'
                joga = 2
                Teste_ganhador(jogador_1, 'x')
            else:
                clear()
                print('Esse local já foi escolhido, tente novamente')
                jogo()
    else:
        play = int(input('''
Jogador = {nome}
Macador = O
Referência:
   0_|_1_|_2
   3_|_4_|_5
   6 | 7 | 8
 
--------------------------------
Jogo Atual
{0}_|_{1}_|_{2}
{3}_|_{4}_|_{5}
{6} | {7} | {8}
Digite a Coordenada da sua jogada: ''' .format(*tabuleiro, nome = jogador_2)))
        if play < 0 or play >9:
            print('Opção Inválida!')
            jogo()
        else:
            if not tabuleiro[play]:
                tabuleiro[play] = 'O'
                joga = 1
                Teste_ganhador(jogador_2, 'O')
            else:
                print('Esse local já foi escolhido, tente novamente')
                jogo()
               
jogo()
