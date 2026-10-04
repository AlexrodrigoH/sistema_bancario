import os
from datetime import datetime

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
def registro_para_extrato(nome, valor, operacao, saldo):
    hora_atual = datetime.now()
    data_hora = hora_atual.strftime("%d/%m/%y %H:%M")
    caminho = open(f"clientes/{nome}/extrato.txt", "a")
    caminho.write(f"{operacao} - {data_hora} - R${float(valor):.2f} - saldo R${float(saldo):.2f}\n")
    caminho.close()
def extrato(nome):
    caminho = open(f"clientes/{nome}/extrato.txt", "r")
    ler_arquivo = caminho.read()
    caminho.close()
    return ler_arquivo