
##Faça um programa que leia e valide as seguintes informações:

##Nome: maior que 3 caracteres;
##Idade: entre 0 e 150;
##Salário: maior que zero;
##Sexo: 'f' ou 'm';
##Estado Civil: 's', 'c', 'v', 'd';

lista_estado_civil = ['S','C','V','D']
lista_sexo = ['F','M']

nome = str(input('Digite o Nome: '))
while True:
    if len(nome) < 3:
        print('Nome menor do que 3 caracteres')
        nome = str(input('Digite o Nome: '))
    else:
        break

idade = int(input('Digite a idade: '))
while True:
    if idade <0 or idade > 150:
        print('Idade fora do limite')
        idade = int(input('Digite a idade: '))
    else:
        break

salario = float(input('Digite o salário: '))
while True:
    if salario <=0:
        print('O salário não pode ser zero')
        salario = float(input('Digite o salário: '))
    else:
        break
      
sexo = str(input('Digite o sexo: '))
while True:
    if sexo.upper().strip() not in lista_sexo:
        print('Sexo Inválido')
        sexo = str(input('Digite o sexo: '))
    else:
        break
                           
estado_civil = str(input('Digite o estado civil: '))
while True:
    if estado_civil.upper().strip() not in lista_estado_civil:
        print('Estado civil inválido!')
        estado_civil = str(input('Digite o estado civil: '))
    else:
        break

print('Cadastrado com Sucesso!')
            
            
                      
            













