import networkx as nx
import matplotlib.pyplot as plt

def min_vertex_cover_approximation(graph: nx.Graph):
    tamanho_nos = {no: len(graph.edges(no)) for no in graph}
    cover = set()

    while tamanho_nos:
        fila_nos = [no for no in tamanho_nos.keys()]
        fila_nos.sort(key=lambda no: tamanho_nos[no])
        # Escolhe o vértice com maior valor
        vert = fila_nos.pop()

        tamanho_nos.pop(vert)
        cover.add(vert)
        for vizinho in graph.neighbors(vert):
            if vizinho not in tamanho_nos:
                continue
            tamanho_nos[vizinho] -= 1.5
            if tamanho_nos[vizinho] <= 0:
                tamanho_nos.pop(vizinho)

    return cover

# Carrega o grafo a partir do arquivo sjdr.gml
graph: nx.Graph = nx.read_gml("sjdr.gml")

# Encontra a cobertura mínima aproximada
cameras = min_vertex_cover_approximation(graph)
no_cameras = set(graph.nodes()) - cameras

# Exibe o resultado
print("Esquinas com câmeras:", cameras)

# Desenha o grafo completo com as câmeras destacadas
pos = nx.spring_layout(graph)  # Posicionamento dos nós para visualização
nx.draw(graph, pos, with_labels=True, font_weight='bold', node_color='g', node_size=500)
nx.draw_networkx_nodes(graph, pos, nodelist=cameras, node_color='r', node_size=500)
plt.show()
