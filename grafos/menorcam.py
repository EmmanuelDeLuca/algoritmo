################################# Dijkstra ###############################
'''class Mais_Curto:
    def __init__(self, tamanho):
        self.aresta = []
        self.peso = []
        self.antecessor = []
    def relaxado(self, u, v, peso):
        if self.peso[v] > self.peso[u] + peso:
            self.antecessor[v] = u
            self.peso[v] = self.peso[u] + peso

    def DIJKSTRA(self, g, w, s):
        for v in range(len(g)):
            self.peso[v] = 999999
            self.antecessor[v] = -1

        self.peso[s] = 0
        conjunto_soluc = []
        #heap_minimo
        funcao = []
        while funcao:
            u = funcao.pop()
            #heap_min
            conjunto_soluc.append(u)
            self.relaxado(u, v, w)'''

################################################ Algoritmo Bellman-Ford ####################################
'''class Mais_Curto:
    def __init__(self, tamanho):
        self.aresta = []
        self.peso = []
        self.antecessor = []
    def relaxado(self, u, v, peso):
        if self.peso[v] > self.peso[u] + peso:
            self.antecessor[v] = u
            self.peso[v] = self.peso[u] + peso

    def DIJKSTRA(self, g, w, s):
        for v in range(len(g)):
            self.peso[v] = 999999
            self.antecessor[v] = -1

        self.peso[s] = 0
        conjunto_soluc = []
        #heap_minimo
        funcao = []
        while funcao:
            u = funcao.pop()
            #heap_min
            conjunto_soluc.append(u)
            self.relaxado(u, v, w)

    def ciclos_negativos(self):
        for i in range(1, len(self.aresta)):
            ##### nao entendi ######
            self.relaxado(v, u, w)

        if self.peso[v] > self.peso[u] + w:
            return False
        else:
            return True
'''