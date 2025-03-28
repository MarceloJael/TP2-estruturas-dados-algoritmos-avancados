def criar_matriz_adjacencia(cidades, conexoes, direcionado=False):
    n = len(cidades)
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    cidade_idx = {cidade: i for i, cidade in enumerate(cidades)}

    for origem, destino in conexoes:
        i, j = cidade_idx[origem], cidade_idx[destino]
        matriz[i][j] = 1
        if not direcionado:
            matriz[j][i] = 1  # simétrico se não direcionado

    return matriz

def exibir_matriz(matriz, cidades):
    print("  ", " ".join(cidades))
    for i, linha in enumerate(matriz):
        print(cidades[i], " ".join(map(str, linha)))

# Dados do grafo
cidades = ["A", "B", "C", "D"]
estradas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]

# Grafo não direcionado
print("Matriz de Adjacência - Grafo NÃO Direcionado:")
matriz_nd = criar_matriz_adjacencia(cidades, estradas, direcionado=False)
exibir_matriz(matriz_nd, cidades)

# Grafo direcionado
print("\nMatriz de Adjacência - Grafo Direcionado:")
matriz_d = criar_matriz_adjacencia(cidades, estradas, direcionado=True)
exibir_matriz(matriz_d, cidades)
