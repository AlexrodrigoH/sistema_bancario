import opcoes_menu
import valida_entrada

print("*** Bem vindo ao BANCO IMAGINARIO*** \n\n")

while True:
      print("1 - Adicionar Clientes\n"
            "2 - Pesquisar Clientes\n"#Esta funcao possuira a opcao de ver dados
            "3 - ver lista de clientes\n" 
            "4 - Sair/Finalizar")
      menu = input("Opcao: ").strip().lower()
      menu = valida_entrada.validar_num(menu)
      print("============Validar entrada: ", menu)
      sair = opcoes_menu.opcao_menu(menu)
      print("============Teste menu -> ", menu)
      if sair == False:
            print("ENCERRANDO BANCO!\n")
            break
      else:
            continue