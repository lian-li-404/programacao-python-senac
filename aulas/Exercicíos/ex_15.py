## Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: • salário bruto. • quanto pagou ao INSS.
# • quanto pagou ao sindicato. • o salário líquido. • calcule os descontos e o salário líquido, conforme a tabela abaixo: Salário Bruto : R$ IR (11%) : R$ INSS (8%) : R$ Sindicato ( 5%) : R$ Salário Liquido : R$ Obs.: Salário Bruto - Descontos = Salário Líquido.

salario_hora = float(input("Quanto Você Ganha Por Hora? "))
horas_trabalhadas = int(input("Digite Quantas Horas Você Trabalhou Esse Mês: "))

salario_bruto = horas_trabalhadas * salario_hora

desconto_ir = (salario_bruto * 0.11) 
desconto_inss = (salario_bruto * 0.8)
desconto_sindicato = (salario_bruto * 0.5)
descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - descontos

print(f'Seu salário bruto foi de: R${salario_bruto:.2f}\nDesconto de IR: R${desconto_ir:.2f}\nDesconto de sindicato: R${desconto_sindicato:.2f}\n Seu salário liquido é de: {salario_liquido:.2f}')
