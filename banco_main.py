import adicionar_clientes


print("*** Bem vindo ao BANCO IMAGINARIO*** \n\n")
print("1 - Adicionar Clientes\n"
      "2 - Pesquisar Clientes\n"#Esta funcao contera a opcao de ver dados
      "3 - Deletar Cliente\n" \
      "4 - Verificar total de clientes\n" \
      "5 - Sair/Finalizar")
nome_do_cliente = input("Nome completo: ").strip().upper()
adicionar_clientes.novo_cliente(nome_do_cliente + ".txt")