import opcoes_menu
import validar_entradas

print("*** Bem vindo ao BANCO IMAGINARIO*** \n\n")

while True:
      print("1 - Adicionar Clientes\n"
            "2 - Pesquisar Clientes\n"#Esta opcao possui submenu de opcoes
            "3 - ver lista de clientes\n" 
            "4 - Sair/Finalizar")
      menu = input("Opcao: ").strip().lower()
      referencia = validar_entradas.Validar_entradas(menu)
      if not referencia.validar_num():
            continue
      if int(menu) <= 0 or int(menu) > 4:
            print("ERROR 001M- Opcao invalida!")
            continue
      sair = opcoes_menu.opcao_menu(int(menu))
      if not sair:
            print("ENCERRANDO BANCO!\n")
            break
      else:
            continue