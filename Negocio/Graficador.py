import networkx as network
import matplotlib.pyplot as gestor


def dibujar(grafo):
    grafico = network.DiGraph()
    for index in grafo.getElementos():
        vertice = grafo.obtener(index)
        grafico.add_node(vertice.getId(), nombre=vertice.getNombre())
        for arista in vertice.getConectados():
            grafico.add_edge(index, arista)

    network.draw(grafico)
    gestor.show()
    network.draw(grafico)
    gestor.savefig("grafico.png")
