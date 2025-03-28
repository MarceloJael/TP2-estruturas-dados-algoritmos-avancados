class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_aresta(self, origem, destino):
        if origem not in self.adjacencia:
            self.adjacencia[origem] = []
        if destino not in self.adjacencia:
            self.adjacencia[destino] = []
        self.adjacencia[origem].append(destino)
        self.adjacencia[destino].append(origem)  # Grafo não direcionado

    def mostrar_lista(self):
        for bairro, vizinhos in self.adjacencia.items():
            print(f"{bairro} -> {vizinhos}")

    def vizinhos_de(self, bairro):
        return self.adjacencia.get(bairro, [])

# Criar grafo e adicionar conexões
grafo = Grafo()
grafo.adicionar_aresta("Centro", "Bairro A")
grafo.adicionar_aresta("Centro", "Bairro B")
grafo.adicionar_aresta("Bairro A", "Bairro C")
grafo.adicionar_aresta("Bairro B", "Bairro C")
grafo.adicionar_aresta("Bairro C", "Bairro D")

# Mostrar lista de adjacência
print("Lista de Adjacência:")
grafo.mostrar_lista()

# Consultar vizinhos
bairro_consulta = "Bairro C"
print(f"\nVizinhos de {bairro_consulta}: {grafo.vizinhos_de(bairro_consulta)}")
