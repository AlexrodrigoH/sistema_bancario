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
            print("\nInforme o nome do cliente que deseja pesquisar: \n")
            nome = input("Nome completo: ").strip().upper().split()
            passou = valida_entrada.validar_str(nome)
            if passou:
                nome = " ".join(nome)
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
                        return print("Funcao ainda nao implementada!\n")
            else:
                print("===========Teste saida de funcao teste submenu!\n")
                break
    elif menu == 5:
        print("\nFINALIZANDO BANCO IMAGINARIO\n")
        print("\n== FIM DA EXECUCAO TESTE ==\n")
        return False