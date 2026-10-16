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
    def executar(self, cliente):
        if self.tipo == "DEPOSITO":
            if self.valor <= 0:
                print(f"Valores {self.valor} nao sao permitidos!\n")
                return False
            else:
                cliente.saldo += self.valor
                return True
        elif self.tipo == "SAQUE":
            if cliente.saldo <= 0 or self.valor > cliente.saldo:
               print(f"Saldo insuficiente! SALDO: {cliente.saldo}\n")
               return False
            else:
                cliente.saldo -= self.valor
                return True
class Clientes_registro:
    def __init__(self, extrato):
        self.extrato = extrato
    def registro(self):
        return {"extrato": self.extrato}
        