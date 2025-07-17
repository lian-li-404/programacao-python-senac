# Faça um Programa que leia três números e mostre o maior e o menor deles.

lista_numero = []

n1 = int(input("Digite o primeiro número: "))
lista_numero.append(n1)
n2 = int(input("Digite o segundo número: "))
lista_numero.append(n2)
n3 = int(input("Digite o terceiro número: "))
lista_numero.append(n3)

print(f'O MAIOR número é: {max(lista_numero)}')
print(f'O MENOR número é: {min(lista_numero)}')

