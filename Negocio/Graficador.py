import networkx as network
import matplotlib.pyplot as gestor


# metodo que visualiza el grafo en la pantalla
# mediante la libreria networkx
def dibujar(grafo):
    grafico = network.DiGraph()  # utiliza la libreria para crea un objeto grafo
    for index in grafo.getElementos():
        vertice = grafo.obtener(index)
        # utiliza la libreria para añadir un nodo al objetp grafo
        grafico.add_node(vertice.getId(), nombre=vertice.getNombre())
        for arista in vertice.getConectados():
            # utiliza la libreria para enlazar un nodo con otro
            grafico.add_edge(index, arista)

    # utiliza la libreria para pintar el objeto grafo
    network.draw(grafico)
    gestor.show()
    network.draw(grafico)
    # utiliza la libreria para guarda el objeto grafo en formato png
    gestor.savefig("grafico.png")
