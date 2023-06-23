############################## Arvore ##################################
class NodaArvore:
    def __init__(self,nome, valor):
        self.nome = nome
        self.ponto = valor
        self.filho_esquerda = None
        self.filho_direita = None

class Arvore:
    def __init__(self, raiz = None, elemento = None):
        if elemento == None:
            self.raiz = elemento
        elif raiz != None:
            self.raiz = None
        else:
            aux = NodaArvore(raiz)
            self.raiz = aux
        self.tamanho = 0

    def adicionar_arvore(self, nome, ponto):
        jogador = None
        corredor = self.raiz
        while corredor != None:
            jogador = corredor 
            if ponto > corredor.ponto:
                corredor = corredor.filho_direita
            else:
                corredor = corredor.filho_esquerda
        if jogador == None:
            self.raiz = NodaArvore(nome,ponto)
        elif ponto > jogador.ponto:
            jogador.filho_direita = NodaArvore(nome, ponto)
        else:
            jogador.filho_esquerda = NodaArvore(nome, ponto)


    def buscar_arvore(self,ponto):
        return self._buscar_arvore(ponto, self.raiz)

    def _buscar_arvore(self, ponto, aux):
        if aux == None:
            return aux

        if aux.ponto == ponto:
            return Arvore(aux)

        elif ponto > aux.ponto:
            return self._buscar_arvore(ponto, aux.filho_direita)

        elif ponto < aux.ponto:
            return self._buscar_arvore(ponto, aux.filho_esquerda)

        else:
            return 'nao tem ngm'

    def prox_arvore(self, ponto):
        pass
        # mostrar sucessor e predecessor



def main():
    comandok = int(input('comando: '))
    aux = Arvore()
    for i in range(comandok):
        entrada = input('entrada: ').split()
        nome = entrada[1]
        ponto = int(entrada[2])
        if entrada[0] == 'ADD':
            if aux.buscar_arvore(ponto) == ponto:
                print('{} ja esta no sistema.'.format(nome))
                aux.adicionar_arvore(nome,ponto)
                print('{} inserido com sucesso!'.format(nome))
            else:
                aux.adicionar_arvore(nome,ponto)
                print('{} inserido com sucesso!'.format(nome))   
        else:
            aux.prox_arvore()

if __name__ == '__main__':
    main()
####################################################################
