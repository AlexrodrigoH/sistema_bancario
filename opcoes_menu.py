import os
import adicionar_clientes
import valida_entrada
import json

def opcao_menu(menu):
    #adiciona novos clientes, caso o cliente ja exista, ele nao sera adicionado.
    if menu == 1:
        while True:
            nome = input("Nome completo: ").strip().upper()
            escolha = valida_entrada.validar_str(nome)
            if escolha:
                adicionar_clientes.novo_cliente(nome)
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
                with open("local_clientes/dados_clientes.json", "r", encoding="utf-8") as arquivo:
                    nome_ind = json.load(arquivo)
                print("\nANTES DO IF DIGITO\n")
                if nome_indice.isdigit():
                    print("\nENTROU NO IF DIGITO\n")
                    digito_valido = valida_entrada.validar_num(nome_indice)
                    tam = len(nome_ind["clientes"])
                    if int(nome_indice) < 1 or int(nome_indice) > tam:
                        print(f"Indice invalido! Total de indices cadastrados: {tam}")
                        continue
                    elif digito_valido:
                            nome = nome_ind["clientes"][int(nome_indice)-1]["nome"]
                            passou = True
                            break
                    else:
                        continue
                palavra_valida = valida_entrada.validar_str(nome_indice)
                print("\nANTES DO IF PALAVRA\n")
                if palavra_valida:
                    print("\nDENTRO DO IF PALAVRA\n")
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
                    if opcao == 1:
                        while True:
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
                                new_saldo = adicionar_clientes.pesquisar_clientes(nome)
                                if new_saldo:
                                    caminho = open(f"clientes/{nome}/saldo.txt", "r")
                                    saldo = caminho.read()
                                    caminho.close()
                                    if saldo == "":
                                        saldo = 0
                                    saldo = float(saldo)
                                    valor += saldo
                                adicionar_clientes.adiciona_saldo(nome, valor)
                                adicionar_clientes.registro_para_extrato(nome, deposito, "deposito", valor)
                                print(f"Deposito de R${deposito} realizado com sucesso!\n")

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
                                new_saldo = adicionar_clientes.pesquisar_clientes(nome)
                                if new_saldo:
                                    caminho = open(f"clientes/{nome}/saldo.txt", "r")
                                    saldo = caminho.read()
                                    caminho.close()
                                    if saldo == "":
                                        saldo = 0
                                        saldo = float(saldo)
                                    if valor > float(saldo):
                                        print("Saldo insuficiente!\n")
                                        print(f"Saldo atual: R${float(saldo):.2f}\n")
                                        break
                                    else:
                                        valor = float(saldo) - valor
                                        verificacao = adicionar_clientes.adiciona_saldo(nome, valor, "saque")
                                        if not verificacao:continue
                                        print(f"Saque de R${saque} realizado com sucesso!\n")
                                        break
                    elif opcao == 3:
                        extrato = adicionar_clientes.extrato(nome)
                        if extrato == "":
                            print("Nao ha movimentacoes!\n")
                        else:
                            print(f"Extrato do cliente {nome}:\n{extrato}\n")
                            continue
                    elif opcao == 4:
                        print("Voltando ao menu principal!\n")
                        return True
    elif menu == 3:
        clientes = os.listdir("clientes")
        print(f"\nClientes cadastrados: {len(clientes)}\n")
        posicao = 1
        teste_dicionario = []
        while True:
            print("1 - Listar clientes\n"
                  "2 - Selecionar cliente\n"
                  "3 - Voltar ao menu principal\n")
            while True:
                opcao_menu_3 = input("Opcao do menu-> ").strip().upper()
                opcao_menu_3 = valida_entrada.validar_num(opcao_menu_3)
                if not opcao_menu_3:
                    continue
                else:
                    break
            if opcao_menu_3 == 1:
                for lista in clientes:
                    arquivo = open(f"clientes/{lista}/saldo.txt", "r")
                    saldo_geral = arquivo.read()
                    arquivo.close()
                    print(f"{posicao} - {lista} \n") #Saldo: R${float(saldo_geral):.2f}\n")
                    posicao+= 1
                    teste_dicionario.append({"nome": lista, "saldo": saldo_geral})
            elif opcao_menu_3 == 2:
                while True:
                    indice_cliente = input("Digite o numero/nome do cliente: ").strip().upper()
                    if indice_cliente.isdigit():
                        passou_num = valida_entrada.validar_num(indice_cliente)
                        if not passou_num:
                            continue
                        else:
                            if int(indice_cliente) > len(clientes):
                                print("Indeice nao encontrado!\n")
                                continue
                            else:
                                print(f"\nCliente selecionado: {teste_dicionario[int(indice_cliente) - 1]['nome']}\nSALDO: R${float(teste_dicionario[int(indice_cliente) - 1]['saldo']):.2f}\n")  # Exemplo: selecionando o cliente
                                break
                    else:
                        passou_num = indice_cliente.split()
                        permitido = valida_entrada.validar_str(passou_num)
                        if not permitido:
                            continue
                        if not adicionar_clientes.pesquisar_clientes(indice_cliente):
                            print("Nome de cliente incorreto ou nao cadastrado!")
                            continue
                        else:
                            for nomes in teste_dicionario:
                                if nomes["nome"] == indice_cliente:
                                    print(f"\n Cliente: {nomes['nome']}"
                                          f"\n SALDO: R$ {float(nomes['saldo'])}")
                                    break
                    break
    elif menu == 4:
        print("\nFINALIZANDO BANCO IMAGINARIO\n")
        print("\n== FIM DA EXECUCAO TESTE ==\n")
        return False