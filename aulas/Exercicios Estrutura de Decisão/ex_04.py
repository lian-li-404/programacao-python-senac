## Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogais = ['a','e','i','o','u']

letra = str(input("Digite uma letra: "))
if letra not in vogais:
    print(f"A letra {letra} é uma consoante")
else:
    print(f"A letra {letra} é vogal")