
class Carro:
    def __init__(self, nome):
        self.nome = nome
        pass 

    def acelerar(self):
        print(f'{self.nome} está acelerando ....')


fusca = Carro('Fusca')

print(f'Nome: {fusca.nome}')

fusca.acelerar()

byd = Carro('BYD')
print('Nome: ', byd.nome)
byd.acelerar()