import Modelo.Estructura as modelo


# metodo que contruye un nuevo grafo
def construir():
    grafo = modelo.Grafo()
    grafo.agregar("Universidad Autónoma Gabriel Rene Moreno", -17.775530, -63.195854)
    grafo.agregar("La Ramada", -17.793336, -63.188160)
    grafo.agregar("Centro Comercial Chiriguano", -17.790315, -63.205503)
    grafo.agregar("Cine Center", -17.798327, -63.179034)
    grafo.agregar("Las Brisas Centro Comercial", -17.749140, -63.175953)
    grafo.agregar("Centro Comercial Ventura Mall", -17.754422, -63.199559)
    grafo.agregar("Monumento Cristo Redentor", -17.770142, -63.182428)
    grafo.agregar("Catedral Metropolitana Basílica Menor de San Lorenzo de Santa Cruz", -17.783820, -63.181833)
    return unir(grafo)


# metodo que enlaza todos los elementos del grafo
def unir(grafo):
    grafo.enlazar(0, 4, 0, 8)
    grafo.enlazar(0, 1, 0, 5)
    grafo.enlazar(1, 5, 0, 3)
    grafo.enlazar(1, 2, 0, 4)
    grafo.enlazar(1, 3, 0, 7)
    grafo.enlazar(2, 7, 0, 5)
    grafo.enlazar(2, 6, 0, 9)
    grafo.enlazar(3, 0, 2, 5)
    grafo.enlazar(5, 2, 0, 2)
    grafo.enlazar(6, 3, 0, 3)
    grafo.enlazar(7, 6, 0, 9)
    return grafo


# metodo que imprime todos los elementos del grafo en consola
def imprimir(grafo):
    for elemento in grafo:
        print(elemento)
