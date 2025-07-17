## Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = int(input("Digite um número: "))
if numero < 0:
    print(f'O número {numero} é negativo!')
elif numero >=0:
    print(f'O número {numero} é positivo!')