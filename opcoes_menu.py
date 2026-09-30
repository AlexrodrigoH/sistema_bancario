import adicionar_clientes
import valida_entrada

def opcao_menu(menu):
    if menu == 1:
        while True:
            nome = input("Nome completo: ").strip().upper().split()
            escolha = valida_entrada.validar_str(nome)
            if escolha:
                nome = " ".join(nome)
                adicionar_clientes.novo_cliente(nome + ".txt")
                print("Cliente adicionado com sucesso!\n")
                return True
            else:
                continue
    if menu == 5:
                print("\nFINALIZANDO BANCO IMAGINARIO\n")
                print("\n== FIM DA EXECUCAO TESTE ==\n")
                return False