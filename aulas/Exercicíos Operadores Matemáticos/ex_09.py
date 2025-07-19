# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

graus = int(input("Digite Os Graus Para Converter: "))
fahrenheit = (graus * 1.8) + 32
print(f"A Temperatura em Fahrenheit é {fahrenheit:.0f}")