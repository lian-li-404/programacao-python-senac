## Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

fahrenheit = int(input("Digite a temperatura em Fahrenheit: "))
conversao = (fahrenheit - 32) / 1.8
print(f"A Temperatura em Celsius é de: {conversao:.1f}")
