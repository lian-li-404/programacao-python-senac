
##Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input('Digite uma Nota: '))

while True:
    if nota < 0 or nota > 10:
        nota = int(input('Digite uma Nota: '))
    else:
        print(f'A nota do usuário é: {nota}')
        break
