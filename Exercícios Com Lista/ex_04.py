# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista_vogais = ['a','e','i','o','u']
consoantes = []
qtd_consoantes = 0

for c in range(10):
    caracter = str(input("Digite um caracter: "))
    for letra in caracter:
        if letra not in lista_vogais:
            consoantes.append(letra)
            qtd_consoantes = qtd_consoantes + 1

print(f'Quantidade de Consoantes: {qtd_consoantes}')           
print(f'Lista de Consoantes: {consoantes}')
