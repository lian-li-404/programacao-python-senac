# Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista_numero = []

n1 = int(input("Digite o primeiro número: "))
lista_numero.append(n1)
n2 = int(input("Digite o segundo número: "))
lista_numero.append(n2)
n3 = int(input("Digite o terceiro número: "))
lista_numero.append(n3)

lista_numero.sort()


print(f"O primeiro número é {lista_numero[0]}")

print(f"O segundo número é {lista_numero[1]}")

print(f"O terceiro número é {lista_numero[2]}")