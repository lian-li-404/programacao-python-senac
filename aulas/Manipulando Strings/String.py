
import tkinter as tk

concatenacao =  'Senac' + 'Curso Python'
print(concatenacao)

cinco_vezes_a = 5 * 'a'
print(cinco_vezes_a)

## Formatação

## imc indice massa corporea calculo = peso / altura ** 2

nome = 'Elian Souza de Oliveira'
altura = 1.70
peso = 78
imc = peso / altura ** 2
print(f"{nome}\nTem: {altura} de altura\nPesa: {peso}\nSeu IMC é: {imc:.2f}") ## Com o fstring "2f" significa o número de casas decimais
print(f"{nome}\nTem: {altura} de altura\nPesa: {peso}\nSeu IMC é: {imc}") ## Sem o fstring 


