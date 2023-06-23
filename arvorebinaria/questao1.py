
class Node:
    def __init__(self, nome, ponto):
        self.esquerda = None
        self.direita = None
        self.pai = None
        self.ponto = ponto
        self.nome = nome


    def adicionar_arvore(self, root, nome, ponto):
        if root is None:
            return Node(nome,ponto)
        else:
            if root.ponto == ponto:
                return root
            elif root.ponto < ponto:
                root.direita = self.adicionar_arvore(root.direita, nome,ponto)
            else:
                root.esquerda = self.adicionar_arvore(root.esquerda, nome, ponto)
        return root
    
    def buscar_arvore(self, raiz, nome, chave):
        if raiz is None:
            return False

        if raiz.ponto == chave or raiz.nome == nome:
            return True

        if raiz.ponto < chave:
            return self.buscar_arvore(raiz.direita, nome, chave)

        return self.buscar_arvore(raiz.esquerda, nome, chave)

    
    def buscar_arvore2(self, raiz, chave):
        if raiz is None:
            return False

        if raiz.ponto == chave:
            return raiz

        if raiz.ponto < chave:
            return self.buscar_arvore2(raiz.direita, chave)

        return self.buscar_arvore2(raiz.esquerda, chave)

    
    def minimo_valor(self, raiz):
        if raiz == None:
            return None
        else:
            while raiz.esquerda != None:
                raiz = raiz.esquerda
            return raiz.nome
    
    def maximo_valor(self, raiz):
        if raiz == None:
            return None
        else:
            while raiz.direita != None:
                raiz = raiz.direita
            return raiz.nome
        
    def sucessor(self, raiz):
        if raiz == None:
            return None
        if raiz.direita != None:
            return self.minimo_valor(raiz.direita)

        y = raiz.pai
        while y != None and raiz == y.direita:
            raiz = y
            y = raiz.pai
        
        return y

    def predecessor(self, raiz):
        if raiz == None:
            return None
        if raiz.esquerda != None:
            return self.maximo_valor(raiz.esquerda)

        y = raiz.pai
        while y != None and raiz == y.esquerda:
            raiz = y
            y = raiz.pai

        return y


def main():
    comandok = int(input())
    controle_add = 0
    for i in range(comandok):
        entrada = input().split()
        if entrada[0] == 'ADD':
            nome = entrada[1]
            ponto = int(entrada[2])
            if controle_add == 0:
                controle_add += 1
                aux = Node(nome, ponto)
                print('{} inserido com sucesso!'.format(nome))
            else:
                if aux.buscar_arvore(aux, nome, ponto) == True:
                    print('{} ja esta no sistema.'.format(nome))
                else:
                    aux.adicionar_arvore(aux, nome,ponto)
                    print('{} inserido com sucesso!'.format(nome))  
        else:
            ponto = int(entrada[1])
            raiz = aux.buscar_arvore2(aux, ponto)
            if aux.predecessor(raiz) == None and aux.sucessor(raiz) == None:
                print('Apenas {} existe no sistema...'.format(raiz.nome))

            elif aux.sucessor(raiz) != None and aux.predecessor(raiz) == None:
                print("{} e o menor! e logo apos vem {}".format(raiz.nome, aux.sucessor(raiz)))

            elif aux.sucessor(raiz) == None and aux.predecessor(raiz) != None:
                print("{} e o maior! e logo atras vem {}".format(raiz.nome, aux.predecessor(raiz)))

            elif aux.sucessor(raiz) != None and aux.predecessor(raiz) != None:
                print("{} vem apos {} e antes de {}".format(raiz.nome, aux.predecessor(raiz), aux.sucessor(raiz)))

if __name__ == '__main__':
    main()


'''print('O sucessor de {} é {}'.format(nome.nome, aux.sucessor(nome)))'''


'''def inorder(root):
    if root:
        inorder(root.esquerda)
        print(root.ponto)
        inorder(root.direita)

r = Node('eze', 50)
r = r.adicionar_arvore(r,'axul', 30)
r = r.adicionar_arvore(r,'verde', 20)
r = r.adicionar_arvore(r,'triti',40)
r = r.adicionar_arvore(r, 'rosa', 70)
r = r.adicionar_arvore(r, 'tratu', 60)
r = r.adicionar_arvore(r,'riberin', 80)


inorder(r)

print(r.buscar_arvore(r, 'axul', 30))'''