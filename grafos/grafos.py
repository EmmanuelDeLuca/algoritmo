#################################GRAFOS##########################################
class Grafos_greifos:
    def __init__(self, vertices, arestas):
        self.v = vertices
        self.a = arestas

    def adjc(self, v):
        return self.a[v]

    def dfs(self, origem):
        lista = [origem]
        visitados = []
        while lista:
            vertice = lista.pop()
            if vertice in visitados:
                continue
            visitados.append(vertice)
            for v in self.a[vertice]:
                lista.append(v)

        return len(visitados)
    
    def bfs(self, origem):
        aux = 1
        visitados = len(self.v) * [False]
        antecessor = [-1] * len(self.v)
        fila = []

        visitados[origem - 1] = True
        fila.append(origem)

        while fila:
            v = fila.pop()

            for i in self.adjc(v):
                if visitados[i-1] == False:
                    visitados[i-1] = True
                    fila.append(i)
                    antecessor[i-1] = v
                    aux += 1

        return aux


    




def main():
    entrada = input().split()
    qtd_usuarios = int(entrada[0])
    qtd_conexoes = int(entrada[1])
    vertices = []
    arestas = [[]for _ in range(qtd_usuarios+1)]
    for i in range(1, qtd_usuarios+1):
        vertices.append(i)

    for i in range(qtd_conexoes):
        conexoes = input().split()
        conex1 = int(conexoes[0])
        conex2 = int(conexoes[1])
        arestas[conex1].append(conex2)
        arestas[conex2].append(conex1)
    g = Grafos_greifos(vertices, arestas)
    output = ''
    for i in range(1, qtd_usuarios+1):
        output += ' ' + str(g.dfs(i))
    
    print(output.strip())
    print(arestas)
    print(vertices)

if __name__ == '__main__':
    main()