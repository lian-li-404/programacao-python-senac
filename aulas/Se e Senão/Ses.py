## if e else
chuva = True
if chuva:
    print("Abrir Guarda-Chuva")
else:
    print("Deixa Guarda-Chuva na Bolsa")


## elif + Validação de entrada
entrada = input("Você quer entrar ou sair? ")
entrada = entrada.lower()
if entrada == "entrar":
    print("Seja Bem Vindo, Entrou no Sistema!")
elif entrada == "sair":
    print("Até Mais...")
else:
    print("Você não digitou 'entrar' ou 'sair' ")

