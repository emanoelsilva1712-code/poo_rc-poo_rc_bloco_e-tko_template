from abc import ABC, abstractmethod

class Pagamento(ABC):
    def __init__(self, valor: float, descricao: str):
        self.valor: float = valor
        self.descricao: str = descricao
    
    def validar_valor(self):
        if self.valor <= 0:
            raise ValueError("Valor negativo")
    
    def resumo(self):
        return f"Pagamento de R$ {self.valor}: {self.descricao}"
    
    @abstractmethod
    def processar(self):
        pass

class Pix(Pagamento):
    def __init__(self, valor: float, descricao: str, chave: str, banco: str):
        super().__init__(valor, descricao)
        self.chave = chave
        self.banco = banco

    def processar(self):
        print(f"Pagando pix produto {self.descricao} para {self.chave} do banco {self.banco} no valor de {self.valor}")
    
class CartaoCredito(Pagamento):
    def __init__(self, valor: float, descricao: str, numero: int, nome_titular: str, limite_disponivel: int):
        self.numero: int = numero
        self.nome_titular = nome_titular


def processar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    pagamento.resumo()
    pagamento.processar()

pix = Pix(2.50, "café coado", "123", "pikipeiii")
processar_pagamento(pix)