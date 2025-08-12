## Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas = []
media_maior_7 = 0

for aluno in range(10):
    for n in range(4):
        nota = float(input(f'Digite a {n+1}º nota: '))
        notas.append(nota)
    print('---------------------------------------')
    
    soma = sum(notas)
    media = soma / 4
    if media >=7:
        media_maior_7 = media_maior_7 + 1
    
print(f'O total de alunos com média maior ou igual a 7 foi de: {media_maior_7}')