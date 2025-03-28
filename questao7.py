from collections import deque

# Lista de Adjacência - Grafo não direcionado
grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["C", "F"],
    "F": ["D", "E"]
}

# Exibir lista de adjacência
print("Lista de Adjacência (Grafo das Cidades):")
for cidade, vizinhos in grafo.items():
    print(f"{cidade} -> {vizinhos}")

# BFS - Busca em Largura
def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    ordem = []

    while fila:
        cidade = fila.popleft()
        if cidade not in visitados:
            visitados.add(cidade)
            ordem.append(cidade)
            for vizinho in grafo[cidade]:
                if vizinho not in visitados:
                    fila.append(vizinho)
    return ordem

# DFS - Busca em Profundidade
def dfs(grafo, inicio, visitados=None, ordem=None):
    if visitados is None:
        visitados = set()
    if ordem is None:
        ordem = []

    visitados.add(inicio)
    ordem.append(inicio)

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados, ordem)

    return ordem

# Testes
print("\nOrdem de visitação (BFS a partir de A):", bfs(grafo, "A"))
print("Ordem de visitação (DFS a partir de A):", dfs(grafo, "A"))