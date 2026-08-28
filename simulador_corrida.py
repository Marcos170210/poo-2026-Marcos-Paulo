from abc import ABC, abstractmethod


class Veiculo(ABC):

    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass



class Carro(Veiculo):

    def acelerar(self):
        print(f"Carro {self.modelo}: acelerando rapidamente pelas pistas!")



class Moto(Veiculo):

    def acelerar(self):
        print(f"Moto {self.modelo}: acelerando com muita agilidade!")



class Caminhao(Veiculo):

    def acelerar(self):
        print(f"Caminhão {self.modelo}: acelerando com força e transportando sua carga!")


class CarroEletrico(Veiculo):

    def acelerar(self):
        print(f"Carro elétrico {self.modelo}: acelerando silenciosamente com seu motor elétrico!")



pista_de_corrida = [
    Carro("Toyota Corolla"),
    Moto("Honda CB 500"),
    Caminhao("Volvo FH"),
    CarroEletrico("Tesla Model 3")
]


print("=== SIMULAÇÃO DE CORRIDA ===")

for veiculo in pista_de_corrida:
    veiculo.acelerar()

print("============================")