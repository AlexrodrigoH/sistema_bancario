import opcoes_menu

print("*** Bem vindo ao BANCO IMAGINARIO*** \n\n")
while True:
      print("1 - Adicionar Clientes\n"
            "2 - Pesquisar Clientes\n"#Esta funcao contera a opcao de ver dados
            "3 - Deletar Cliente\n" \
            "4 - Verificar total de clientes\n" \
            "5 - Sair/Finalizar")
      while True:
            menu = input("-> ").strip().lower()
            if not menu.isdigit():
                  print("Somente o numero do menu e permitido!\n")
                  print("numeros entre 1 a 5!")
                  continue
            menu = int(menu)
            if menu <= 0 or menu > 5:
                  print("ERROR! Menu possui 5 opcoes!\n")
                  continue
            else:
                  opcoes_menu.opcao_menu(menu)
                  break
      if menu == 5:
            print("\nFINALIZANDO BANCO IMAGINARIO\n")
            print("\n== FIM DA EXECUCAO TESTE ==\n")
            break
      else:
            continue
      