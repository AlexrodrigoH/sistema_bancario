import os
from datetime import datetime
import json
#Cria um novo cliente, criando uma pasta com o nome do cliente e dois arquivos dentro dela, 
# um para o saldo e outro para o extrato.
def novo_cliente(nome):
    if not os.path.exists("local_clientes"):
            os.mkdir(f"local_clientes")
    if not os.path.exists("local_clientes/dados_clientes.json"):
        with open("local_clientes/dados_clientes.json", "x", encoding="utf-8") as arquivo:
            json.dump({"clientes":[]}, arquivo, indent=4, ensure_ascii=False)
    with open("local_clientes/dados_clientes.json", "r", encoding="utf-8") as arquivo:
        cliente_arquivo = json.load(arquivo)
        cliente = cliente_arquivo["clientes"]
    cliente.append({"nome": nome, "saldo": 0, "extrato":[]})
    with open("local_clientes/dados_clientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(cliente_arquivo, arquivo, indent=4, ensure_ascii=False)
#Adiciona saldo ao cliente, caso o cliente nao exista nem chega a esta funcao, 
#pois a funcao pesquisar_clientes() ja verifica se o cliente existe.
def pesquisa_clientes(nome):
    with open("local_clientes/dados_clientes.json", "r", encoding="utf-8") as arquivo:
        conteudo = json.load(arquivo)
    str_nome = str(nome)
    if str_nome.isdigit():
        return conteudo["clientes"][int(nome)-1]["nome"]
    else:
        for pessoa in conteudo["clientes"]:
                if pessoa["nome"] == nome:
                    return nome
def retorna_conteudo():
     with open("local_clientes/dados_clientes.json", "r", encoding="utf-8") as arquivo:
          dados_arquivo = json.load(arquivo)
          return dados_arquivo