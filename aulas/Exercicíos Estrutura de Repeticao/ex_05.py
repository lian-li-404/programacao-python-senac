## Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#  Valide a entrada e permita repetir a operação.

taxa_a = float(input('Digite o Pecentual de Crescimento do País "A": '))
taxa_a_percent = taxa_a/100
taxa_b = float(input('Digite o Pecentual de Crescimento do País "B": '))
taxa_b_percent = taxa_b/100
pop_a = int(input('Digite o número populacional do país "A": '))
pop_b = int(input('Digite o número populacional do país "B": '))

anos = 0

while True:
    if pop_a < pop_b:
        pop_a = (pop_a * taxa_a_percent) + pop_a
        anos = anos + 1
    else:
        print(f'O país A levaria {anos} anos para ter um total de {pop_a:.0f} habitantes. ')
        break