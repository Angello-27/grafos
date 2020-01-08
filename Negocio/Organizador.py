import Modelo.Estructura as modelo


def construir():
    grafo = modelo.Grafo()
    grafo.agregar(100, "Universidad Autónoma Gabriel Rene Moreno", -17.775530, -63.195854)
    grafo.agregar(300, "La Ramada", -17.793336, -63.188160)
    grafo.agregar(400, "Centro Comercial Chiriguano", -17.790315, -63.205503)
    grafo.agregar(800, "Cine Center", -17.798327, -63.179034)
    grafo.agregar(900, "Las Brisas Centro Comercial", -17.749140, -63.175953)
    grafo.agregar(200, "Centro Comercial Ventura Mall", -17.754422, -63.199559)
    grafo.agregar(500, "Monumento Cristo Redentor", -17.770142, -63.182428)
    grafo.agregar(700, "Catedral Metropolitana Basílica Menor de San Lorenzo", -17.783820, -63.181833)
    return unir(grafo)


def unir(grafo):
    grafo.enlazar(100, 300, peso=10, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(400, 300, peso=20, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(100, 400, peso=30, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    # grafo.enlazar(8, 1, 0, 3)
    # grafo.enlazar(11, 3, 0, 4)
    # grafo.enlazar(2, 9, 0, 7)
    # grafo.enlazar(2, 4, 0, 5)
    # grafo.enlazar(9, 23, 0, 9)
    # grafo.enlazar(23, 8, 2, 5)
    # grafo.enlazar(23, 4, 0, 2)
    # grafo.enlazar(11, 8, 0, 3)
    # grafo.enlazar(3, 2, 0, 9)
    return grafo


def imprimir(grafo):
    for elemento in grafo:
        print(elemento)
