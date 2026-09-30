import opcoes_menu
import valida_entrada

print("*** Bem vindo ao BANCO IMAGINARIO*** \n\n")

while True:
      print("1 - Adicionar Clientes\n"
            "2 - Pesquisar Clientes\n"#Esta funcao possuira a opcao de ver dados
            "3 - Deletar Cliente\n" \
            "4 - Verificar total de clientes\n" \
            "5 - Sair/Finalizar")
      menu = input("Opcao: ").strip().lower()
      menu = valida_entrada.validar_num(menu)
      print("Validar entrada: ", menu)
      sair = opcoes_menu.opcao_menu(menu)
      print("Tetse menu -> ", type(menu))
      if sair == False:
            print("ENCERRANDO BANCO!\n")
            break
      else:
            continue