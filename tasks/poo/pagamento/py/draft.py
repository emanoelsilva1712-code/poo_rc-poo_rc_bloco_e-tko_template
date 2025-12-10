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
        super().__init__(valor, descricao)
        self.numero: int = numero
        self.nome_titular = nome_titular
        self.limite_disponivel = limite_disponivel

    def processar(self):
        if self.valor > self.limite_disponivel:
            print(f"Erro: Limite insuficiente no cartão {self.numero}")
            return
        else:
            self.limite_disponivel = self.limite_disponivel - self.valor
            print(f"Pagamento aprovado no cartão Cliente {self.nome_titular}. Limite restante: {self.limite_disponivel}")

class Boleto(Pagamento):
    def __init__(self, valor: float, descricao: str, codigo_barras: float, vencimento: int):
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento

    def processar(self):
        print("Boleto gerado. Aguardando pagamento...")


def processar_pagamento(pagamento: Pagamento):
    pagamento.validar_valor()
    pagamento.resumo()
    pagamento.processar()

pix = Pix(2.50, "café coado", "123", "pikipeiii")
processar_pagamento(pix)

cartao_aprovado = CartaoCredito(150.00, "Livro Python Avançado", 1111, "Maria S", 300)
processar_pagamento(cartao_aprovado)

boleto = Boleto(75.50, "Mensalidade Academia", 987654321, 20261230)
processar_pagamento(boleto)

cartao_negado = CartaoCredito(500.00, "Tênis", 2222, "João P", 100)
processar_pagamento(cartao_negado)