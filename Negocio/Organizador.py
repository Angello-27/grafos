import Modelo.Estructura as modelo


def construir():
    grafo = modelo.Grafo()
    grafo.agregar("Universidad UAGRM")
    grafo.agregar("Segundo elemento")
    grafo.agregar("Tercer elemento")
    grafo.agregar("Cuarto elemento")
    grafo.agregar("Quinto elemento")
    grafo.agregar("Sexto elemento")

    grafo.enlazar(3, 0, 2, 5)
    grafo.enlazar(0, 1, 0, 5)
    grafo.enlazar(1, 2, 0, 4)
    grafo.enlazar(2, 1, 0, 9)
    grafo.enlazar(0, 5, 0, 9)
    grafo.enlazar(1, 5, 0, 3)
    grafo.enlazar(0, 4, 0, 8)
    grafo.enlazar(4, 3, 0, 6)
    grafo.enlazar(2, 1, 0, 9)
    grafo.enlazar(4, 5, 0, 1)
    grafo.enlazar(1, 3, 0, 3)
    grafo.enlazar(4, 3, 0, 2)
    grafo.enlazar(1, 3, 0, 7)
    grafo.enlazar(2, 5, 0, 5)
    grafo.enlazar(0, 2, 0, 2)
    return grafo


def imprimir(grafo):
    for elemento in grafo:
        print(elemento)
