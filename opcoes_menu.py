import os
import adicionar_clientes
import valida_entrada
import json
from datetime import datetime
import clientes

def opcao_menu(menu):
    #adiciona novos clientes, caso o cliente ja exista, ele nao sera adicionado.
    if menu == 1:
        while True:
            nome = input("Nome completo: ").strip().upper()
            escolha = valida_entrada.validar_str(nome)
            if escolha:
                new_cliente = clientes.Clientes(nome)
                clientes.Clientes.atribui_valor(new_cliente)
                adicionar_clientes.novo_cliente(new_cliente)
                print("Cliente adicionado com sucesso!\n")
                return True
            else:
                continue
    #Busca o cliente pelo nome ou pelo indice, caso seja digitado um numero, 
    #ele busca pelo indice, caso seja digitado um nome, ele busca pelo nome.
    elif menu == 2:
        while True:
            while True:
                print("\nInforme o nome do cliente ou numero de cadastro: \n")
                nome_indice = input("Nome completo/indice: ").strip().upper()
                passou = False
                nome_ind = adicionar_clientes.retorna_conteudo()
                #print("\nANTES DO IF DIGITO\n")
                if nome_indice.isdigit():
                    #print("\nENTROU NO IF DIGITO\n")
                    digito_valido = valida_entrada.validar_num(nome_indice)
                    tam = len(nome_ind["clientes"])
                    if int(nome_indice) < 1 or int(nome_indice) > tam:
                        print(f"Indice invalido! Total de indices cadastrados: {tam}")
                        continue
                    elif digito_valido:
                            nome_indice = nome_ind["clientes"][int(nome_indice)-1]["nome"]
                            passou = True
                            break
                    else:
                        continue
                palavra_valida = valida_entrada.validar_str(nome_indice)
                if palavra_valida:
                    teste_nome = False
                    for pessoa in nome_ind["clientes"]:
                        if pessoa["nome"] == nome_indice:
                            passou = True
                            teste_nome = True
                            break
                    if not teste_nome:
                        print("Nome nao encontrado!\n")
                        continue
                    elif teste_nome:
                        print("Sucesso nome encontrado!\n")
                        break
                    else:
                        print("Nome ou indice incorretos!\n")
                        continue
            if passou:
                print(f"Cliente {nome_indice} encontrado!\n")
                #submenu do cliente, onde ele pode fazer deposito, 
                #saque, ver extrato ou voltar ao menu principal.
                while True:
                    print("MENU DO CLIENTE: \n" 
                    "1 - Deposito\n"
                    "2 - Saque\n" 
                    "3 - Extrato\n"
                    "4 - Voltar ao menu principal\n")
                    while True:
                        menu_cliente = input("Opcao: ").strip().lower()
                        opcao = valida_entrada.validar_num(menu_cliente)
                        if not opcao:
                            continue
                        else:
                            break
                    opcao = int(menu_cliente)
                    if opcao == 1:
                        while True:
                            #extrato = []
                            try:
                                deposito = input("Valor do deposito: ").strip()
                                valor = float(deposito)
                            except ValueError:
                                print("Somente numeros!\n")
                                continue
                            if valor <=0:
                                print("Valor deve ser positivo!\n")
                                continue
                            else:
                                for pessoa in nome_ind["clientes"]:
                                    if pessoa["nome"] == nome_indice:
                                        print(f"\nTIPO SALDO {pessoa["saldo"]}")
                                        new_saldo = pessoa["saldo"] + valor
                                        new_atributo = clientes.Clientes_acoes("DEPOSITO", valor)
                                        pessoa["saldo"] = new_saldo
                                        data = datetime.now().strftime("%d/%m/%y - %H:%M")
                                        #movimentacao = new_atributo.atributo_cliente()
                                        movimentacao = {"DATA": data}
                                        movimentacao.update(new_atributo.atributo_cliente())
                                        movimentacao["SALDO"] = pessoa["saldo"]
                                        pessoa["extrato"].append(movimentacao)
                                        with open("local_clientes/dados_clientes.json", "w", encoding="utf-8") as arquivo:
                                            json.dump(nome_ind, arquivo, indent=4, ensure_ascii=False)
                                        print(f"Deposito de R${valor:.2f} realizado com sucesso!\n")
                                        break
                            break
                    elif opcao == 2:
                        while True:
                            try:
                                saque = input("Valor a sacar: R$").strip()
                                valor = float(saque)
                            except ValueError:
                                print("Digite apenas numeros!\n")
                                continue
                            if valor <= 0:
                                print("Valor deve ser positivo!\n")
                                continue
                            else:
                                for pessoa in nome_ind["clientes"]:
                                    if pessoa["nome"] == nome_indice:
                                        if pessoa["saldo"] < valor:
                                            print(f"Saldo insuficiente! Saldo atual: R${pessoa["saldo"]:.2f}\n")
                                            break
                                        else:
                                            pessoa["saldo"] -= valor
                                            novo_mov = clientes.Clientes_acoes("SAQUE", valor)
                                            data = datetime.now().strftime("%d/%m/%y - %H:%M")
                                            movimentacao = {"DATA": data}
                                            movimentacao.update(novo_mov.atributo_cliente())
                                            movimentacao["SALDO"] = pessoa["saldo"]
                                            pessoa["extrato"].append(movimentacao)
                                            with open("local_clientes/dados_clientes.json", "w", encoding="utf-8") as arquivo:
                                                json.dump(nome_ind, arquivo, indent=4, ensure_ascii=False)
                                            print(f"Saque de R${valor:.2f} realizado com sucesso!\n")
                                            break
                            break
                    elif opcao == 3:
                        for pessoa in nome_ind["clientes"]:
                            if pessoa["nome"] == nome_indice:
                                if pessoa["extrato"] == []:
                                    print(f"\nCliente {nome_indice} nao possui movimentacoes!\n")
                                    break
                                else:
                                    for leitura_extrato in pessoa["extrato"]:
                                        print(f"{leitura_extrato["DATA"]} - Tipo: {leitura_extrato["tipo"]} - valor: R${leitura_extrato["valor"]:.2f} - SALDO ATUAL:  R${leitura_extrato["SALDO"]:.2f}\n")
                                    print("\nLeitura finalizada!\n")
                                    break
                    elif opcao == 4:
                        print("Voltando ao menu principal!\n")
                        return True
    elif menu == 3:
        posicao = 1
        if not os.path.exists("local_clientes"):
            print("Primeiro deve adicionar pelo menos 1 cliente!\n")
            return True
        elif not os.path.exists("local_clientes/dados_clientes.json"):
            print("Dados de clientes nao existem, deve adicionar um cliente!\n")
            return True
        nome_ind = adicionar_clientes.retorna_conteudo()
        if not nome_ind["clientes"]:
            print("Nao ah clientes cadastrados!\n")
            return True
        else:
            print("="*20)
            print("\nLista de clientes cadastrados: \n")
            print("="*20,"\n")
            for pessoa in nome_ind["clientes"]:
                if pessoa["nome"]:
                    print(f"{posicao} - {pessoa["nome"]}")
                    posicao += 1
                    continue
                else:
                    break
            print("\n\n")
            return True
    elif menu == 4:
        print("\nFINALIZANDO BANCO IMAGINARIO\n")
        print("\n== FIM DA EXECUCAO TESTE ==\n")
        return False