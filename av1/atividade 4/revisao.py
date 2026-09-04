class Veiculos:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self._valor_diaria = valor_diaria
    def get_valor_diaria(self): 
        return self._valor_diaria
    def calcular_aluguel(self, dias):
        return self.get_valor_diaria() * dias 

class Carro(Veiculo):
    def_init_(self, marca, modelo, valor_diaria, portas):