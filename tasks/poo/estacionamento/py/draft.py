from abc import ABC, abstractmethod
import math

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

    def calcularValor(self, horaSaida: int) -> float:
        return 3.00    #valor fixo

class Moto(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Moto", horaEntrada)

    def calcularValor(self, horaSaida: int) -> float:
        tempo_estacionado = horaSaida - self.horaEntrada

        if tempo_estacionado <= 0:
            return 0.00

        valor = tempo_estacionado / 20.0
        return valor

class Carro(Veiculo):
    def __init__(self, id: str, horaEntrada: int):
        super().__init__(id, "Carro", horaEntrada)

    def calcularValor(self, horaSaida: int) -> float:
        tempo_estacionado = horaSaida - self.horaEntrada

        if tempo_estacionado <= 0:
            return 5.00
        
        valor = tempo_estacionado / 10.0
        return max(valor, 5.00)

class Estacionamento:
    def __init__(self):
        self.veiculosEstacionados: dict[str, Veiculo] = {}
        self.horaAtual = 0

    def setTempo(self, tempo: int):
        self.horaAtual += tempo

    def estacionar(self, tipo: str, id: str):
        if id in self.veiculosEstacionados:
            print(f"Erro: veiculo {id} já está está estacionado.")
            return
        
        hora_entrada = self.horaAtual
        if tipo.lower() == "bike":
            veiculo = Bike(id, hora_entrada)
        elif tipo.lower() == "moto":
            veiculo = Moto(id, hora_entrada)
        elif tipo.lower() == "carro":
            veiculo = Carro(id, hora_entrada)
        else:
            print(f"Erro: Tipo de veiculos {tipo} desconhecido.")
            return 
        
        self.veiculosEstacionados[id] = veiculo

    def pagar(self, id: str):
        if id not in self.veiculosEstacionados:
            print(f"Veiculo {id} não está estacionado.")
            return 

        veiculo = self.veiculosEstacionados.pop(id)
        hora_saida = self.horaAtual
        valor = veiculo.calcularValor(hora_saida)
        print(f"{veiculo.tipo} chegou {veiculo.horaEntrada} saiu {hora_saida}. Pagar R$ {valor:.2f}")

    def __str__(self):
        output = ""

        def ordem_tipo(tipo):
            if tipo == "Bike":
                return 1
            elif tipo == "Moto":
                return 2
            elif tipo =="Carro":
                return 3
            return 99

        veiculos_ordenados = sorted(self.veiculosEstacionados.values(), key=lambda v: (ordem_tipo(v.tipo), v.id))

        for veiculo in veiculos_ordenados:
            output += f"{veiculo}\n"

        output += f"Hora atual: {self.horaAtual}"
        return output.strip()

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
            if len(args) == 2:
                try:
                    tempo = int(args[1])
                    estacionamento.setTempo(tempo)
                except ValueError:
                    print("Erro: Tempo invalido.")

        elif args[0] == "estacionar":
            if len(args) == 3:
                tipo = args[1]
                id = args[2]
                estacionamento.estacionar(tipo, id)
            else:
                print("Erro: Uso: estacionar <tipo> id>")

        elif args[0] == "pagar":
            if len(args) == 2:
                id = args[1]
                estacionamento.pagar(id)
            else:
                print("Erro: Uso: pagar <id>")


main()

