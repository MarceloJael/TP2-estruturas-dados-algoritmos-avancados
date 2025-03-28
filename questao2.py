import networkx as nx
import matplotlib.pyplot as plt

# Lista de Adjacência
grafo = {
    "Centro": ["Bela Vista", "Jardim"],
    "Bela Vista": ["Centro", "Industrial", "Vila Nova"],
    "Jardim": ["Centro", "São João"],
    "Industrial": ["Bela Vista", "São João"],
    "São João": ["Jardim", "Industrial", "Vila Nova"],
    "Vila Nova": ["Bela Vista", "São João"]
}

# Visualização com networkx
G = nx.Graph()
for bairro, vizinhos in grafo.items():
    for vizinho in vizinhos:
        G.add_edge(bairro, vizinho)

print("Bairros e conexões (Lista de Adjacência):")
for bairro, vizinhos in grafo.items():
    print(f"{bairro} -> {vizinhos}")

# Desenhar o grafo
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=2000, font_size=10)
plt.title("Mapa dos Bairros - Grafo da Cidade")
plt.show()
