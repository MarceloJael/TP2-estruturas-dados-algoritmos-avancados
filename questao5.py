from collections import deque

class Grafo:
    def __init__(self):
        self.adjacente = {}

    def adicionar_aresta(self, origem, destino, peso=1):
        if origem not in self.adjacente:
            self.adjacente[origem] = []
        if destino not in self.adjacente:
            self.adjacente[destino] = []
        self.adjacente[origem].append((destino, peso))
        self.adjacente[destino].append((origem, peso))  # Grafo não direcionado

    def mostrar_vizinhos(self):
        for centro, vizinhos in self.adjacente.items():
            print(f"{centro} -> {vizinhos}")

    def bfs_rota_mais_curta(self, inicio, destino):
        visitado = set()
        fila = deque([[inicio]])

        while fila:
            caminho = fila.popleft()
            no = caminho[-1]
            if no == destino:
                return caminho
            if no not in visitado:
                visitado.add(no)
                for vizinho, _ in self.adjacente.get(no, []):
                    novo_caminho = list(caminho)
                    novo_caminho.append(vizinho)
                    fila.append(novo_caminho)
        return None

# Criar grafo com pesos (tempo médio de transporte)
grafo = Grafo()
grafo.adicionar_aresta("A", "B", 10)
grafo.adicionar_aresta("A", "C", 8)
grafo.adicionar_aresta("B", "D", 6)
grafo.adicionar_aresta("C", "E", 12)
grafo.adicionar_aresta("D", "E", 7)

# Exibir vizinhos
print("Vizinhos de cada centro:")
grafo.mostrar_vizinhos()

# Buscar rota mais curta entre A e E
rota = grafo.bfs_rota_mais_curta("A", "E")
print(f"\nRota mais curta de A até E (por BFS): {rota}")