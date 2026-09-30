def validar_str(validacao):
    if validacao == "":
         return False
    for palavra_valido in validacao:
        if palavra_valido.isalpha():
            continue
        else:
            print("Nome invalido! Inserir somente nomes validos!!\n")
            return False
    return True
def validar_num(valido_num):
    if not valido_num.isdigit():
        print("Somente numeros!\n")
        return False
    valido_num = int(valido_num)
    if valido_num <= 0 or valido_num > 5:
            print("ERROR! Menu possui 5 opcoes!\n")
            return False
    else:
         return valido_num