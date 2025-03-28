import time

# Grafo com 1000 vértices e 10 arestas
vertices = 1000
arestas = [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9),
           (10, 11), (12, 13), (14, 15), (16, 17), (18, 19)]

# Matriz de adjacência
matriz = [[0] * vertices for _ in range(vertices)]
for u, v in arestas:
    matriz[u][v] = 1
    matriz[v][u] = 1

# Lista de adjacência
lista = {i: [] for i in range(vertices)}
for u, v in arestas:
    lista[u].append(v)
    lista[v].append(u)

# Verificar vizinhos do vértice 0
print("Vizinhos na lista:", lista[0])
print("Vizinhos na matriz:", [i for i in range(vertices) if matriz[0][i] == 1])

# Tempo para verificar se (0,1) existe
start = time.time()
existe_matriz = matriz[0][1] == 1
tempo_matriz = time.time() - start

start = time.time()
existe_lista = 1 in lista[0]
tempo_lista = time.time() - start

print(f"\nAresta (0,1) existe na matriz? {existe_matriz} (tempo: {tempo_matriz:.10f})")
print(f"Aresta (0,1) existe na lista? {existe_lista} (tempo: {tempo_lista:.10f})")
