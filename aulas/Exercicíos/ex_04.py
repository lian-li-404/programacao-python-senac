# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input("Digite a Primeira Nota: "))
n2 = float(input("Digite a Segunda Nota: "))
n3 = float(input("Digite a Terceira Nota: "))
n4 = float(input("Digite a Quarta Nota: "))

total = n1 + n2 + n3 + n4
media = total / 4
print(f"A média é: {media:.2f}")