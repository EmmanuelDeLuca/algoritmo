#################### Lista Encadeada ########################
class NodaLista:
    def __init__(self, valor):
        self.dado = valor
        self.anterior = None
        self.posterior = None

class Listaduplamente:
    def __init__(self):
        self.comeco = None
        self.tamanho = 0
#################### inserção Na frente da DLL ########################
    def push(self, x):
        novo_dado = NodaLista(x)
        novo_dado.posterior = self.comeco
        novo_dado.anterior = None
        if self.comeco != None:
            self.comeco.anterior = novo_dado

        self.comeco = novo_dado

#################### Adicionar um nó após um determinado nó ########################
    def inserirNo(self, prev_no, x):
        if prev_no == None:
            print('Esse nó nao existe na lista')
            return
        novo_dado = NodaLista(x)
        novo_dado.posterior = prev_no.posterior
        prev_no.posterior = novo_dado
        novo_dado.anterior = prev_no
        if novo_dado.posterior:
            novo_dado.posterior.anterior = novo_dado

#######################  Adicione um nó no final ###################################
    def inserirfinal(self, x):
        novo_dado = NodaLista(x)

        if self.comeco == None:
            self.comeco = novo_dado
            return

        ponteiro = self.comeco
        while ponteiro.posterior != None:
            ponteiro = ponteiro.posterior

        ponteiro.posterior = novo_dado
        novo_dado.anterior = ponteiro

##################### EXCLUINDO O NÓ ###############################    
    def deletno(self, delet):
        if (self.comeco == None) or (delet == None):
            return
        if self.comeco == delet:
            self.comeco = delet.posterior

        if delet.posterior != None:
            delet.posterior.anterior = delet.anterior
        
        if delet.anterior != None:
            delet.anterior.posterior = delet.posterior

    def printList(self):
        temp = self.comeco
        while temp != None:
            print(temp.dado, end= ' -> ')
            temp = temp.posterior
        
        print()



#################### inserção Na frente da DLL ########################
if __name__ == '__main__':
    listaligada = Listaduplamente()
    '''listaligada.inserirfinal(6)
    listaligada.push(7)
    listaligada.push(1)
    listaligada.inserirfinal(4)'''


    
    

