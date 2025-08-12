# Faça um Programa que leia um vetor A com 10 números inteiros, 
# calcule e mostre a soma dos quadrados dos elementos do vetor.

numeros = []
quadrados = []

for c in range(10):
    numero = int(input(f"Digite o {c+1}º: "))
    numeros.append(numero)

for numero in numeros:
    quadrado = numero ** 2 
    quadrados.append(quadrado)

print(f'A soma dos quadrados é: {sum(quadrados)}')