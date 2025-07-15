#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Quanto Você Ganha Por Hora? "))
carga_horaria = int(input("Digite Sua Carga Horária: "))
dias_trabalhados = int(input("Digite Quantos Dias Você Trabalhou: "))
salario = (salario_hora * carga_horaria) * dias_trabalhados

print(f"Seu Salário é de R$ {salario:.2f}")
