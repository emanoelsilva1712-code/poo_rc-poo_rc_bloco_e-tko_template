from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome: str =  nome
        
    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}!")

    @abstractmethod
    def fazer_som(self):    #metodo abstrato
        pass

    @abstractmethod
    def mover(self):     #metodo abstrato
        pass

class Leao(Animal):     #subclass que obdece a class base (Animal)
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("miaaaal")

    def mover(self):
        print("caminhada")

class Elefante(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Truuuu")

    def mover(self):
        print("bum (andando)")

class Cobra(Animal):
    def __init__(self, nome: str):
        super().__init__(nome)

    def fazer_som(self):
        print("Ssssss")

    def mover(self):
        print("rasteja")

def apresentar(animal: Animal):
    #chama os métodos
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()
    print(f"Tipo de Objeto: {type(animal).__name__}")

if __name__ == "__main__":

    simba = Leao("Simba")
    bolota = Elefante("Bolota")
    juditi = Cobra("Juditi")
