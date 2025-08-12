import time
# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas = []
for c in range(4):
    nota = float(input(f'Digite a {c+1}º nota: '))
    notas.append(nota)

soma_notas = sum(notas)
media = soma_notas / 4

for n in notas:
    print(f'As notas são: {n}')
    time.sleep(1)

print(f'E a média é de: {media}')