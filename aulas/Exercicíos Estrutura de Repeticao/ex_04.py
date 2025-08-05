##Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
#Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

taxa_a = 0.03
taxa_b = 0.015
pop_a = 80000
pop_b = 200000

anos = 0

while True:
    if pop_a < pop_b:
        pop_a = (pop_a * taxa_a) + pop_a
        anos = anos + 1
    else:
        print(f'O país A levaria {anos} anos para ter um total de {pop_a:.0f} habitantes. ')
        break