"""

    Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:

    Salário Bruto até 900 (inclusive) - isento

    Salário Bruto até 1500 (inclusive) - desconto de 5%

    Salário Bruto até 2500 (inclusive) - desconto de 10%

    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220) : R$ 1100,00 (-) IR (5%) : R$ 55,00
    (-) INSS ( 10%) : R$ 110,00 FGTS (11%) : R$ 121,00 Total de descontos : R$ 165,00 Salário Liquido : R$ 935,00

"""

salario_hora = float(input("Digite seu salário por hora: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
salario_bruto = horas_trabalhadas * salario_hora

desconto_ir = 0
desconto_inss = salario_bruto *0.10

if salario_bruto <=900.00:
    desconto_ir = salario_bruto * 0
elif salario_bruto >900.00 and salario_bruto <=1500.00:
    desconto_ir = salario_bruto * 0.05
elif salario_bruto >1500 and salario_bruto <=2500.00:
    desconto_ir = salario_bruto * 0.10
elif salario_bruto > 2500:
    desconto_ir = salario_bruto * 0.20

print(f'Total de descontos: R${desconto_ir+desconto_inss:.2f}')
total_descontos = desconto_ir + desconto_inss
print(f'Salário Liquido: R${salario_bruto-total_descontos:.2f}')



