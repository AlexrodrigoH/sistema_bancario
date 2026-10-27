class Validar_entradas:
    #Objeto para validacao
    def __init__(self, dados):
        self.dados = dados
    #Validacao para palavras
    def validar_str(self):
        if self.dados == "":
            print("ERROR - 000V - Nome invalido!")
            return False
        nome_split = self.dados.split()
        for nome in nome_split:
            cont = 0
            if nome[0] == "'" or nome[-1] == "'":
                print("ERROR - 001V - Nome invalido")
                return False
            for letra in nome:
                if letra == "'":
                    cont += 1
                if cont > 1:
                    print("ERROR - 002V - Nome invalido")
                    return False
        nome_split = self.dados.replace("'", "").split()
        for nome_int in nome_split:
            if not nome_int.isalpha():
                print("ERROR - 003V - Nome invalido!")
                return False
        return self.dados
    #Validacao de numeros inteiros
    def validar_num(self):
        if self.dados == "":
            print("ERROR - 004V - Opcao invalida!")
            return False
        if not self.dados.isdigit():
            print("ERROR - 005V - Opcao invalida!")
            return False
        return True
    #Validacao da estrutura monetaria
    def validar_monetario(self):
        valor = self.dados
        cont = 0
        while valor:
            if valor[0] == "0":
                valor = valor[1:]
                continue
            break
        if self.dados == "":
            print("ERROR - 006V - Valor invalido!")
            return False
        caractere_permitido = "0123456789.,"
        for caractere in valor:
            if caractere not in caractere_permitido:
                print("ERROR - 007V - Valor invalido!")
                return False
        if len(valor) == 1:
            if valor.isdigit():
                valor = valor + ".00"
            else:
                print("ERROR - 008V - Valor invalido!")
                return False
        elif len(valor) == 2:
            if valor[-1] in ",.":
                valor = valor + "00"
            elif valor[0] == "," or valor[0] == ".":
                print("ERROR - 009V - Valor invalido!")
                return False
        elif len(valor) >= 3:
            if valor[-1] in ",.":
                valor = valor + "00"
            if valor[-2] not in ",." and valor[-3] not in ",.":
                valor = valor + ".00"
            if valor[-2] == "," or valor[-2] == ".":
                valor = valor[:-2].replace(",","").replace(".","") + valor[-2:]
            elif valor[-3] == "," or valor[-3] == ".":
                valor = valor[:-3].replace(",","").replace(".","") + valor[-3:]
        valor = valor.replace(",",".")
        try:
            valor = float(valor)
        except ValueError:
            print("ERROR - 010V - Valor invalido!")
            return False
        self.dados = f"{valor:,.2f}".replace(",","x").replace(".",",").replace("x",".")
        return self.dados