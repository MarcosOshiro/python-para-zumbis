'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as
informações
'''

nome = input("Entre com o nome de usuário: ")
senha = input("Entre com a senha: ")

while nome == senha or senha.startswith(nome) or senha.endswith(nome):
    print("ERRO - Nome deve ser diferente da Senha")
    nome = input("Entre com o nome de usuário: ")
    senha = input("Entre com a senha: ")

    
'''
Como foi resolvido no video

usuário = input('Usuário: ')
senha = input('Senha: ')
while usuário = senha:
    print('Senha deve ser diferente do Usuário')
    usuário = input('Usuário: ')
    senha = input('Senha: ')

'''
