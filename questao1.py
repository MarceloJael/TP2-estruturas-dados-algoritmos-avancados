import networkx as nx
import matplotlib.pyplot as plt

# Criar o grafo não direcionado
G = nx.Graph()

# Adicionar vértices e arestas
G.add_edges_from([
    ("Alice", "Bob"),
    ("Alice", "Carlos"),
    ("Bob", "Diana"),
    ("Carlos", "Diana"),
    ("Carlos", "Eduardo")
])

# Exibir vértices e arestas
print("Vértices:", list(G.nodes))
print("Arestas:", list(G.edges))

# Desenhar o grafo
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=10)
plt.title("Rede Social - Grafo de Amizades")
plt.show()
