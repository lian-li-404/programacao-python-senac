# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

media = (nota1+nota2+nota3) / 3

if media >= 7 and media < 10:
    print(f'Parabéns! Sua média é {media} e você está APROVADO')
elif media < 7:
    print(f'Estude Mais! Sua média é {media} e você está REPROVADO')
elif media == 10:
    print(f'Você foi diferenciado! Sua média é {media} e você está APROVADO APROVADO APROVADO')