import opcoes_menu
import valida_entrada

print("*** Bem vindo ao BANCO IMAGINARIO*** \n\n")

while True:
      print("1 - Adicionar Clientes\n"
            "2 - Pesquisar Clientes\n"#Esta opcao possui submenu de opcoes
            "3 - ver lista de clientes\n" 
            "4 - Sair/Finalizar")
      menu = input("Opcao: ").strip().lower()
      if int(menu) <= 0 or int(menu) > 4:
            print("ERROR! Valor invalido!\n")
            continue
      else:
            menu = valida_entrada.validar_num(menu)     
      sair = opcoes_menu.opcao_menu(menu)
      if sair == False:
            print("ENCERRANDO BANCO!\n")
            break
      else:
            continue