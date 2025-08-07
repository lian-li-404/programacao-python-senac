
## Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro.

numero = 0
lista_numero = []

while numero < 20:
    numero = numero + 1
    lista_numero.append(numero)
    print(numero)

while numero < 20:
    numero = numero + 1
    lista_numero.append(numero)

print(str(lista_numero).replace(']','').replace('[',''))