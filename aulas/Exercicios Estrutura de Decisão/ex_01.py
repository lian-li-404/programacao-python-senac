# Faça um Programa que peça dois números e imprima o maior deles.

n1 = int(input("Digite o primeiro número: "))
n2= int(input("Digite o segundo número: "))

if n1 > n2:
    print(f'O maior número é {n1}')
elif n2 > n1:
    print(f'O maior número é {n2}')
elif n1 == n2:
    print("Os números são iguais")