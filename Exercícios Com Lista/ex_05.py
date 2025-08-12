# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
impar = []
par = []

def par_impar(n):
    if n % 2 == 0:
        return "P"
    else:
        return "I"

for n in range(5):
    numero = int(input(f"Digite o {n+1}º: "))
    numeros.append(numero)

for n in numeros:
    if par_impar(n) == 'P':
        par.append(n)
    elif par_impar(n) == 'I':
        impar.append(n)

print(f'O total de números é: {numeros}')
print(f'Os números PAR são: {par}')
print(f'Os números ÍMPAR são: {impar}')