# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

import time

numeros = []

for c in range(5):
    numero = int(input(f"Digite o {c+1}º número: "))
    numeros.append(numero)

for numero in numeros:
    print(f'O número é: {numero}')
    time.sleep(1)
    print(f'A soma é: {numero + numero}')
    time.sleep(1)
    print(f'A multiplicação é: {numero * numero}')
    print('------------------------------------------')