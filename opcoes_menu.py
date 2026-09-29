import adicionar_clientes

def opcao_menu(menu):
    if menu == 1:
        while True:
            nome = input("Nome completo: ").strip().upper().split(" ")
            print("Teste SPLIT: ", nome, "\n")
            for valido in nome:
                if valido.isalpha():
                    continue
                else:
                    print("Nome invalido! Inserir somente nomes validos!!\n")
                    break
            nome = " ".join(nome)
            adicionar_clientes.novo_cliente(nome + ".txt")
            print("Depois de join: ", nome)
            break