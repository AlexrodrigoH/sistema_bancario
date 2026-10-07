import os
from datetime import datetime
#Cria um novo cliente, criando uma pasta com o nome do cliente e dois arquivos dentro dela, 
# um para o saldo e outro para o extrato.
def novo_cliente(arquivo):
    #arquivo = open("clientes/" + arquivo, "w")
    os.mkdir(f"clientes/{arquivo}")
    caminho = open(f"clientes/{arquivo}/saldo.txt", "w")
    if caminho == "":
        caminho.write("0")
    caminho.close()
    caminho = open(f"clientes/{arquivo}/extrato.txt", "w")
    caminho.close()
#Pesquisa se o cliente existe, caso exista, retorna True, caso nao exista, retorna False.
def pesquisar_clientes(nome):
    try:
        #caminho = open(f"clientes/{nome},", "r")
        #caminho.close()
        teste = os.path.exists(f"clientes/{nome}")
        return teste
    except FileNotFoundError:
        print(f"Cliente {nome} nao encontrado!\n")
        return False
#Adiciona saldo ao cliente, caso o cliente nao exista nem chega a esta funcao, 
#pois a funcao pesquisar_clientes() ja verifica se o cliente existe.
def adiciona_saldo(nome, valor):
    caminho = open(f"clientes/{nome}/saldo.txt", "w")
    caminho.write(str(valor))
    caminho.close()
#Registra a operacao no extrato do cliente, para exibicao futura!
def registro_para_extrato(nome, valor, operacao, saldo):
    hora_atual = datetime.now()
    data_hora = hora_atual.strftime("%d/%m/%y %H:%M")
    caminho = open(f"clientes/{nome}/extrato.txt", "a")
    caminho.write(f"{operacao} - {data_hora} - R${float(valor):.2f} - saldo R${float(saldo):.2f}\n")
    caminho.close()
#Exibe o registro de extrato do cliente! Se o conteudo estiver vazio exibe que nao a registro!
def extrato(nome):
    caminho = open(f"clientes/{nome}/extrato.txt", "r")
    ler_arquivo = caminho.read()
    caminho.close()
    return ler_arquivo