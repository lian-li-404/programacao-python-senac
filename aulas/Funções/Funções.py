## Construção de uma função, são utilizadas para diminuir a repetição de comandos, tornando o programa mais limpo 

## Exemplos:

## Print 4 vezes a mesma coisa
print("Olá mudo")
print("Olá mudo")
print("Olá mudo")
print("Olá mudo")

## Print 4 vezes a mesma coisa usando função 

def printar(qtd, str):
    for c in range(0,qtd):
        print(str)

printar(4,"Hello")