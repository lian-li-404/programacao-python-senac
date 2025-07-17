# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
lista_precos = []

n1 = float(input("Digite o preço do primeiro número: "))
lista_precos.append(n1)
n2 = float(input("Digite o preço do segundo número: "))
lista_precos.append(n2)
n3 = float(input("Digite o preço do terceiro número: "))
lista_precos.append(n3)

produto_mais_barato = min(lista_precos)

print(f"Você deve comprar o produto de valor R${produto_mais_barato:.2f} pois é o mais barato")