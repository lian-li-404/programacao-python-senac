import tkinter as tkinter

## AND, OR, IN, NOT IN 
usuario = True
senha = False

## AND 
if usuario == True and senha == True:
    print("Login Realizado!!")
elif usuario == True and senha == False:
    print("Senha Incorreta!!")
elif usuario == False and senha == True:
    print("Usuário Incorreto!!")

## OR 
nome = input("Digite o Seu Nome: ").strip().upper()
if nome == "ELIAN" or nome == "CARLOS":
    print(f"Bem vindo {nome}!")
else:
    print("Seja Bem Vindo Usuário Comum")

## NOT IN E IN 
senha = input("Cadastre uma senha com caracteres especiais: ")
lista_caracteres = []

for letra in senha:
    lista_caracteres.append(letra)
if '@' not in lista_caracteres:
    print("Não possui caracteres especiai!")
elif '@' in lista_caracteres:
    print("Possui lista de caracteres")

