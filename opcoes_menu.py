import os
import adicionar_clientes
import valida_entrada

def opcao_menu(menu):
    if menu == 1:
        while True:
            nome = input("Nome completo: ").strip().upper().split()
            escolha = valida_entrada.validar_str(nome)
            if escolha:
                nome = " ".join(nome)
                adicionar_clientes.novo_cliente(nome)
                print("Cliente adicionado com sucesso!\n")
                return True
            else:
                continue
    elif menu == 2:
        while True:
            print("\nInforme o nome do cliente ou numero de cadastro: \n")
            nome_indice = input("Nome completo/indice: ").strip().upper()
            if nome_indice.isdigit():
                passou_num = valida_entrada.validar_num(nome_indice)
                passou = True
            else:
                nome = nome_indice.split()
                passou = valida_entrada.validar_str(nome)
            if passou:
                nome = " ".join(nome_indice)
                if passou_num:
                    clientes = os.listdir("clientes")
                    if int(nome_indice) > len(clientes):
                        print("Indice nao encontrado!\n")
                        continue
                    else:
                        nome = clientes[int(nome_indice) - 1]
                else:
                    nome = nome_indice
                cliente = adicionar_clientes.pesquisar_clientes(nome)
                if not cliente:
                    print("Cliente nao encontrado!\n")
                    return True
                else:
                    print(f"Cliente {nome} encontrado!\n")
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
                                            adicionar_clientes.adiciona_saldo(nome, valor)
                                            print(f"Saque de R${saque} realizado com sucesso!\n")
                                            adicionar_clientes.registro_para_extrato(nome, saque, "saque", valor)
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
        for lista in clientes:
            arquivo = open(f"clientes/{clientes[posicao - 1]}/saldo.txt", "r")
            saldo_geral = arquivo.read()
            arquivo.close()
            print(f"{posicao} - {clientes[posicao - 1]} \nSaldo: R${float(saldo_geral):.2f}\n")
            posicao+= 1
    elif menu == 4:
        print("\nFINALIZANDO BANCO IMAGINARIO\n")
        print("\n== FIM DA EXECUCAO TESTE ==\n")
        return False