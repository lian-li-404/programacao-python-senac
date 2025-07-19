## Faça um Programa que peça 2 números inteiros e um número real. 
# Calcule e mostre: • o produto do dobro do primeiro com metade do segundo .
#  • a soma do triplo do primeiro com o terceiro. • o terceiro elevado ao cubo.

primeiro_int = int(input("Digite o Primeiro Número Inteiro: "))
segundo_int = int(input("Digite o Segundo Número Inteiro: "))
num_real = float(input("Digite o Número Real: "))

dobro_primeiro = primeiro_int*2
triplo_primeiro = primeiro_int*3
metade_segundo = segundo_int / 2
produto = dobro_primeiro ** metade_segundo
soma_triplo_terceiro = triplo_primeiro + num_real
elevado_cubo = num_real * num_real * num_real

print(f"O Produto É: {produto:.0f}\nA soma do triplo do primeiro com o terceiro é {soma_triplo_terceiro}\nO terceiro elevado ao cubo é: {elevado_cubo}")



