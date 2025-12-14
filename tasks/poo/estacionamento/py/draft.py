from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, horaEntrada: int):
        self.id = id
        self.tipo = tipo
        self.horaEntrada = horaEntrada

    @abstractmethod
    def calcularValor(self, horaEntrada: int) -> float:
        pass

    def __str__(self) -> str:
        tipo_fomatado = self.tipo.rjust(10, '_')
        id_formatado = self.id.rjust(10, '_')

        return f"{tipo_fomatado} : {id_formatado} : {self.horaEntrada}"

class Bike(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Bike", horaEntrada)

    def CalcularValor(self, horaSaida: int) -> float:
        return 3.00    #valor fixo

class Moto(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Moto", horaEntrada)

    def CalcularValor(self, horaSaida: int) -> float:
        tempo_estacionado = horaSaida - self.horaEntrada

        if tempo_estacionado <= 0:
            return 0.00

        valor = tempo_estacionado / 20.0
        return valor

class Carro(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Carro", horaEntrada)

    def CalcularValor(self, horaSaida: int) -> float:
        tempo_estacionado = horaSaida - self.horaEntrada

        if tempo_estacionado <= 0:
            return 5.00
        
        valor = tempo_estacionado / 10.0
        return max(valor, 5.00)

class Estacionamento:
    def __init__(self, veiculo: str, horaAtual: int):
        self.veiculo = veiculo
        self.horaAtual = horaAtual

def main():

    estacionamento = Estacionamento()
    while True:
        try:
            line = input()
        except IOError:
            break

        print("$" + line)
        args = line.split()        

        if args[0] == "end":
            break

        elif args[0] == "show":
            print(estacionamento)

        elif args[0] == "tempo":

        elif args[0] == "estacionar":

        elif args[0] == "pagar":

main()

