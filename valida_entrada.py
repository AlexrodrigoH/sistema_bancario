def validar_str(validacao):
    if validacao == "":
         return False
    nome_splitado = validacao.split()
    for palavra_valido in nome_splitado:
        if not palavra_valido.isalpha():
            print("\nNome invalido! Inserir somente nomes validos!!\n")
            return False
    return True
def validar_num(valido_num):
    if valido_num == "":
             return False
    elif not valido_num.isdigit():
        print("Somente numeros!\n")
        return False
    valido_num = int(valido_num)
    if valido_num <= 0:
        print("ERROR! Somente numeros positivos!\n")
        return False
    return True
def validar_moeda():
     pass