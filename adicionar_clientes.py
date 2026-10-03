import os

def novo_cliente(arquivo):
    #arquivo = open("clientes/" + arquivo, "w")
    os.mkdir(f"clientes/{arquivo}")
    caminho = open(f"clientes/{arquivo}/saldo.txt", "w")
    caminho.close()
    caminho = open(f"clientes/{arquivo}/extrato.txt", "w")
    caminho.close()
def pesquisar_clientes(nome):
    try:
        #caminho = open(f"clientes/{nome},", "r")
        #caminho.close()
        teste = os.path.exists(f"clientes/{nome}")
        return teste
    except FileNotFoundError:
        print(f"Cliente {nome} nao encontrado!\n")
        return False
def adiciona_saldo(nome, valor):
    caminho = open(f"clientes/{nome}/saldo.txt", "w")
    caminho.write(str(valor))
    caminho.close()