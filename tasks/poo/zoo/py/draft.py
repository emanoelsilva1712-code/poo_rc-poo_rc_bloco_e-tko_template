class Animal:
    def __init__(self, nome: str):
        self.__nome = nome

    def apresentar_nome(self):
        print("Eu sou um(a) <nome>!")