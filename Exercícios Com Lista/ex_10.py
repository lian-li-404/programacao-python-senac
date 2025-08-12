## Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

## NÃO CONSEGUI A PARTE FNAL

import random as rd

vetor_1 = []
vetor_2 = []
vetor_3 = []


print("Primeiro Vetor: ")
for c in range(10):
    elemento = input(f"Digite o {c+1}º elemento: ")
    vetor_1.append(elemento)

print("Segundo Vetor: ")
for c2 in range(10):
    elemento = input(f"Digite o {c2+1}º elemento: ")
    vetor_2.append(elemento)
        
for e in vetor_1:
    vetor_3.append(e)

for e in vetor_2:
    vetor_3.append(e)

for index in vetor_3:
    print(index)