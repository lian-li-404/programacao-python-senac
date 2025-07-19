"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

"""
salario = float(input("Digite seu salário: "))
salario_ajustado = 0 

if salario <=279.99:
    ajuste = salario * 0.20
    print(f'Seu salário era de: R${salario:.2f}')
    print(f'Seu salário vai ter um ajuste de 20% (R${ajuste:.2f}) e passará para: R${salario+ajuste:.2f}')
    
elif salario >=280.00 and salario <= 700.00:
    ajuste = salario * 0.15
    print(f'Seu salário era de: R${salario:.2f}')
    print(f'Seu salário vai ter um ajuste de 15% (R${ajuste:.2f}) e passará para: R${salario+ajuste:.2f}')

elif salario >=700.00 and salario <= 1499.99:
    ajuste = salario * 0.10
    print(f'Seu salário era de: R${salario:.2f}')
    print(f'Seu salário vai ter um ajuste de 10% (R${ajuste:.2f}) e passará para: R${salario+ajuste:.2f}')

elif salario >=1500.00 :
    ajuste = salario * 0.05
    print(f'Seu salário era de: R${salario:.2f}')
    print(f'Seu salário vai ter um ajuste de 5% (R${ajuste:.2f}) e passará para: R${salario+ajuste:.2f}')
