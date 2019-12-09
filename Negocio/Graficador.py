import networkx as network
import matplotlib.pyplot as gestor


def mostrar(grafo):
    grafico = network.Graph()
    for index in grafo.getElementos():
        grafico.add_node(index)
        vertice = grafo.obtener(index)
        for arista in vertice.getConectados():
            grafico.add_edge(index, arista)

    network.draw(grafico)
    gestor.show()
    network.draw(grafico)
    gestor.savefig("diseño.png")
