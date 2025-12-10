class Estacionamento:
    def __init__(self, veiculo: str, horaAtual: int):
        self.veiculo = veiculo
        self.horaAtual = horaAtual

from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        self.id = id
        self.tipo = tipo
        self.horaEntrada = horaEntrada

    @abstractmethod
    def calcularValor(self):
        pass

class Bike(Veiculo):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        super().__init__(id, tipo, horaEntrada)

    def CalcularValor(self):


class Moto(Veiculo):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        super().__init__(id, tipo, horaEntrada)

    def CalcularValor(self):


class Carro(Veiculo):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        super().__init__(id, tipo, horaEntrada)

    def CalcularValor(self):

def main():

    estacionamento = Estacionamento()
    while True:
        line = input()
        print("$" + line)
        args = line.split()        

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(estacionamento)


