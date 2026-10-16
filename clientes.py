import os
class Clientes:
    def __init__(self, nome = "", saldo = 0.0):
        self.nome = nome
        self.saldo = saldo  
    def atribui_valor(self):
        return {"nome": self.nome, "saldo": self.saldo}

class Clientes_acoes:
    def __init__(self, tipo, valor):
        self.valor = valor
        self.tipo = tipo
    def atributo_cliente(self):
        return {"tipo": self.tipo, "valor": self.valor}

class Clientes_registro:
    def __init__(self, extrato):
        self.extrato = extrato
    def registro(self):
        return {"extrato": self.extrato}
        