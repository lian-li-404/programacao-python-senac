##Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

soma_nota = n1+n2
media = soma_nota / 2

if media > 9.0 and media <=10.0:
    print(f'Sua média foi de {media}\nO conceito é A e você está APROVADO!')
elif media >=7.5 and media <9.0:
    print(f'Sua média foi de {media}\nO conceito é B e você está APROVADO!')
elif media >=6.0 and media <7.5:
    print(f'Sua média foi de {media}\nO conceito é C e você está APROVADO!')
elif media >=4.0 and media <6.0:
    print(f'Sua média foi de {media}\nO conceito é D e você está REPROVADO!')
elif media <4.0:
    print(f'Sua média foi de {media}\nO conceito é E e você está REPROVADO!')