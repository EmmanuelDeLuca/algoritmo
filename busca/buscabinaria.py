################### BUSCA BINARIA ############################
def buscabinaria(lista,valor):
    if valor > int(lista[-1]):
        return False
    inicio = 0 
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim)//2
        if int(lista[meio]) > valor:
            fim = meio - 1
        elif int(lista[meio]) < valor:      
            inicio = meio + 1

        else: 
            return True
    return False


def main():
    entrada1 = (input( )).split()
    entrada2 = (input( )).split()
    linha1 = ''
    linha2 = ''
    for c in entrada2:
        if buscabinaria(entrada1,int(c)):
          linha1 += str(c) + " "
        else:
          linha2 += str(c) + " "      
    print('{}' .format(linha1))
    print('{}' .format(linha2))
     
if __name__ == '__main__':
    main()
