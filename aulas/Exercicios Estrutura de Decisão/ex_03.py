## Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("Digite F ou M: ")).strip().upper()

if sexo == 'M':
    print('M - Masculino')
elif sexo == 'F':
    print('F - Feminino')
else:
    print('Você não digitou F ou M')

