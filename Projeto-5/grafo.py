import networkx as nx
import matplotlib.pyplot as plt


# A = [[0, 0, 1, 1/2], [1/3, 0, 0, 0], [1/3, 1/2, 0, 1/2], [1/3, 1/2, 0, 0]]

# Matriz de ligação arbitrária para testar o programa (escolhi a matriz A do enunciado).
def desenhaA(A):
    # Lista dos vértices do grafo.
    VERTICES = []
    for x in range(len(A)):
        VERTICES.append(x + 1)
        
    # Lista das arestas do grafo.

    ARESTAS = []

    for coluna in range(len(A[0])):
        for linha in range(len(A)):
            if A[linha][coluna] > 0:
                ARESTAS.append((coluna + 1, linha + 1))
        
    # Desenho do grafo.      
        
    G = nx.DiGraph()
    G.add_nodes_from(VERTICES)   
    G.add_edges_from(ARESTAS)   

    # print("Vértices do grafo: ")
    # print(G.nodes())

    # print("Arestas do grafo, de a para b (a, b): ")
    # print(G.edges())

    nx.draw(G, with_labels = True)   # Desenha o grafo.
    plt.savefig("desenho.png")   # Salva o grafo desenhado como png na pasta do script.
    plt.show()   # Mostra o grafo desenhado.