import networkx as network
import matplotlib.pyplot as gestor


def mostrar(grafo):
    grafico = network.Graph()
    network.draw(grafico)
    gestor.show()
    network.draw(grafico)
    gestor.savefig("diseño.png")
