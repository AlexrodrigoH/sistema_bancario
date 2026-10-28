import os
import adicionar_clientes
import validar_entradas
import json
from datetime import datetime
import clientes

def opcao_menu(menu):
    #adiciona novos clientes, caso o cliente ja exista, ele nao sera adicionado.
    referencia = validar_entradas.Validar_entradas(menu)
    if menu == 1:
        while True:
            nome = input("Nome completo: ").strip().upper()
            referencia.dados = nome
            escolha = referencia.validar_str()
            if escolha:
                new_cliente = clientes.Clientes(nome)
                clientes.Clientes.atribui_valor(new_cliente)
                adicionar_clientes.novo_cliente(new_cliente)
                print("Cliente adicionado com sucesso!\n")
                return True
            else:
                continue
    #Busca o cliente pelo nome ou pelo indice, caso seja digitado um numero, 
    #ele busca pelo indice, caso seja digitado um nome, ele busca pelo nome.
    elif menu == 2:
        while True:
            while True:
                print("\nInforme o nome do cliente ou numero de cadastro: \n")
                nome_indice = input("Nome completo/indice: ").strip().upper()
                referencia.dados = nome_indice
                passou = referencia.validar_num()
                nome_ind = adicionar_clientes.retorna_conteudo()
                cliente_encontrado = False
                if passou:
                    tam = len(nome_ind["clientes"])
                    if int(nome_indice) < 1 or int(nome_indice) > tam:
                        print(f"Indice invalido! Total de indices cadastrados: {tam}")
                        continue
                    else:
                            nome_indice = nome_ind["clientes"][int(nome_indice)-1]["nome"]
                            cliente_encontrado = True
                            referencia.dados = nome_indice
                            break
                if not passou:
                    nome_valido = referencia.validar_str()
                    if nome_valido:
                        for pessoa in nome_ind["clientes"]:
                            if pessoa["nome"] == nome_indice:
                                passou = True
                                cliente_encontrado = True
                                break
                    if not cliente_encontrado:
                        print("Nome nao encontrado!\n")
                        continue
                    elif cliente_encontrado:
                        print("Sucesso nome encontrado!\n")
                        break
            if cliente_encontrado:
                print(f"Cliente {nome_indice} encontrado!\n")
                #submenu do cliente, onde ele pode fazer deposito, 
                #saque, ver extrato ou voltar ao menu principal.
                while True:
                    print("MENU DO CLIENTE: \n" 
                    "1 - Deposito\n"
                    "2 - Saque\n" 
                    "3 - Extrato\n"
                    "4 - Voltar ao menu principal\n")
                    while True:
                        menu_cliente = input("Opcao: ").strip().lower()
                        referencia.dados = menu_cliente
                        opcao_submenu = referencia.validar_num()
                        if not opcao_submenu:
                            continue
                        elif int(opcao_submenu) <= 0 or int(opcao_submenu) > 4:
                            print("ERROR - 001OM - Opcao invalida!")
                            continue
                        else: break  
                    opcao = int(menu_cliente)
                    if opcao == 1:
                        while True:
                            referencia.dados = input("Valor do deposito: ").strip()
                            deposito = referencia.validar_monetario()
                            if deposito:
                                valor = referencia.dados
                                clientes_ref = clientes.Clientes_acoes("DEPOSITO", valor)
                                for pessoa in nome_ind["clientes"]:
                                    if pessoa["nome"] == nome_indice:
                                        clientes.Clientes(pessoa["nome"], pessoa["saldo"])
                                        new_atributo = clientes.Clientes_acoes("DEPOSITO", referencia.arquivar)
                                        new_saldo = clientes.Clientes(nome_indice, pessoa["saldo"])
                                        data = datetime.now().strftime("%d/%m/%y - %H:%M")
                                        movimentacao = {"DATA": data}
                                        movimentacao.update(new_atributo.atributo_cliente())
                                        confirmacao = new_atributo.executar(new_saldo)
                                        if not confirmacao:
                                            print("\n\nFalsa validacao\n\n")
                                            break
                                        movimentacao["SALDO"] = new_saldo.saldo
                                        pessoa["saldo"] = new_saldo.saldo
                                        pessoa["extrato"].append(movimentacao)
                                        with open("local_clientes/dados_clientes.json", "w", encoding="utf-8") as arquivo:
                                            json.dump(nome_ind, arquivo, indent=4, ensure_ascii=False)
                                        print(f"Deposito de R${valor} realizado com sucesso!\n")
                                        break
                            else:
                                continue   
                            break
                    elif opcao == 2:
                        while True:
                            try:
                                saque = input("Valor a sacar: R$").strip()
                                saque = saque.replace(",",".")
                                valor = float(saque)
                            except ValueError:
                                print("Digite apenas numeros!\n")
                                continue
                            if valor <= 0:
                                print("Valor deve ser positivo!\n")
                                continue
                            else:
                                for pessoa in nome_ind["clientes"]:
                                    if pessoa["nome"] == nome_indice:
                                        if pessoa["saldo"] < valor:
                                            print(f"Saldo insuficiente! Saldo atual: R${pessoa["saldo"]:.2f}\n")
                                            break
                                        else:
                                            pessoa["saldo"] -= valor
                                            novo_mov = clientes.Clientes_acoes("SAQUE", valor)
                                            data = datetime.now().strftime("%d/%m/%y - %H:%M")
                                            movimentacao = {"DATA": data}
                                            movimentacao.update(novo_mov.atributo_cliente())
                                            movimentacao["SALDO"] = pessoa["saldo"]
                                            pessoa["extrato"].append(movimentacao)
                                            with open("local_clientes/dados_clientes.json", "w", encoding="utf-8") as arquivo:
                                                json.dump(nome_ind, arquivo, indent=4, ensure_ascii=False)
                                            print(f"Saque de R${valor:.2f} realizado com sucesso!\n")
                                            break
                            break
                    elif opcao == 3:
                        referencia_registro = clientes.Clientes_registro(nome_indice)
                        referencia_registro.registro()
                    elif opcao == 4:
                        print("Voltando ao menu principal!\n")
                        return True
            if not cliente_encontrado:
                print(f"Cliente {nome_indice} nao encontrado!")
                break
    elif menu == 3:
        posicao = 1
        if not os.path.exists("local_clientes"):
            print("Primeiro deve adicionar pelo menos 1 cliente!\n")
            return True
        elif not os.path.exists("local_clientes/dados_clientes.json"):
            print("Dados de clientes nao existem, deve adicionar um cliente!\n")
            return True
        nome_ind = adicionar_clientes.retorna_conteudo()
        if not nome_ind["clientes"]:
            print("Nao ah clientes cadastrados!\n")
            return True
        else:
            print("="*20)
            print("\nLista de clientes cadastrados: \n")
            print("="*20,"\n")
            for pessoa in nome_ind["clientes"]:
                if pessoa["nome"]:
                    print(f"{posicao} - {pessoa["nome"]}")
                    posicao += 1
                    continue
                else:
                    break
            print("\n\n")
            return True
    elif menu == 4:
        print("\nFINALIZANDO BANCO IMAGINARIO\n")
        print("\n== FIM DA EXECUCAO TESTE ==\n")
        return False