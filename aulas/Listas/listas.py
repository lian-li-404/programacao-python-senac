# Lista é um objeto aonde podem ser armazenados conteúdos

# Como criar uma lista? Basta definir o nome da lista e seu conteudo, exemplo: 
frutas = ['maça','banana','laranja']

## também é possível criar uma lista vazia 
frutas = []

## Para adicionar itens a lista pode ser utilizado o comando "append", exemplo:
frutas=[]
input_frutas = str(input('Digite uma fruta: '))
frutas.append(input_frutas)

## Removendo elementos com "remove" e "pop": 
## removendo pelo indice:

frutas_pop = ['Mamão','Melancia','Goiaba']
frutas_pop.pop(2) ## removeu Goiabaz
print(frutas_pop)

frutas_pop = ['Mamão','Melancia','Goiaba']
frutas_pop.remove('Goiaba') ## removeu Goiaba
print(frutas_pop)

## também é possível com o comando "insert", porém o mesmo empurra os demais itens, exemplo:
frutas_insert = ['maça','banana','limão']
frutas_insert.insert(0,'Melão')
print(frutas_insert)

## Para acessar itens na lista basta colocar o nome da lista + [index], o index começa em "0", exemplo:
print(f'A fruta selecionada é: {frutas[0]}')

## Utilizando em conjunto com loop
frutas_loop = []
while True:
    fruta = str(input('Digite o nome de uma fruta para adicionar a sacola ou digite PARAR para encerrar sua lista: ')).strip().upper()
    if fruta != "PARAR":
        frutas_loop.append(fruta)
    elif fruta == 'PARAR':
        break

print(str(frutas_loop).replace('[','').replace(']','').replace("'",'').lower())

