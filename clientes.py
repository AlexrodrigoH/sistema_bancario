import json
import adicionar_clientes
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
        print(f"\n\nVALOR EM cliente.executar {cliente}\n\n")
        if self.tipo == "DEPOSITO":
            if self.valor <= 0:
                print(f"ERROR - 001CA - Valores {self.valor} nao sao permitidos!\n")
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
        leitura = adicionar_clientes.retorna_conteudo()
        for item in leitura["clientes"]:
            if item["nome"] == self.extrato:
                if item["extrato"] == []:
                    print(f"Cliente {self.extrato} nao possui registros!")
                    break
                else:
                    for leitura_extrato in item["extrato"]:
                        print(f"DATA: {leitura_extrato["DATA"]}\nMOVIMENTO: {leitura_extrato["tipo"]}\nVALOR: R${leitura_extrato["valor"]}\nSALDO: {leitura_extrato["SALDO"]}\n")
                    print("--LEITURA FINALIZADA--")
                    break     