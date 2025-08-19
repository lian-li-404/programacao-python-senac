class Animal:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade

    def comer(self):
        print(f'O {self.nome} está comendo')

animal1 = Animal('Girafa','20','20')
animal2 = Animal('Gato','40','10')
animal3 = Animal('Leão','100','1')

animal1.comer()
animal2.comer()
animal3.comer()