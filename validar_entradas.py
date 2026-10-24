class Validar_entradas:
    def __init__(self, dados):
        self.dados = dados
    def validar_str(self):
        if self.dados == "":
            print("ERROR - 000 - Nome invalido!")
            return False
        nome_split = self.dados.split()
        for nome in nome_split:
            cont = 0
            for letra in nome:
                if nome[0] == "'" or nome[-1] == "'":
                    print("ERROR - 001 - Nome invalido")
                    return False
                if letra == "'":
                    cont += 1
                if cont > 1:
                    print("ERROR - 002 - Nome invalido")
                    return False
        nome_split = self.dados.replace("'", "").split()
        for nome_int in nome_split:
            if not nome_int.isalpha():
                print("ERROR - 003 - Nome invalido!")
                return False
        return self.dados
    def validar_num(self):
        pass
    def validar_monetario(self):
        pass