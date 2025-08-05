#Faça um programa que leia um nome de usuário e a sua senha e não aceite 
# a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome_usuario = str(input('Digite seu nome de usuário: '))
senha = str(input('Digite sua senha: '))

while True:
    if nome_usuario in senha:
        print("A sua senha não pode conter o seu nome de usuário")
        senha = str(input('Digite sua senha: '))
    else:
        print('Cadastrado com Sucesso!')
        break