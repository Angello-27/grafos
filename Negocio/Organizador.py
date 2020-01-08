import Modelo.Estructura as modelo


def construir():
    grafo = modelo.Grafo()
    grafo.agregar(100, "Universidad Autónoma Gabriel Rene Moreno", -17.775530, -63.195854)
    grafo.agregar(300, "La Ramada", -17.793336, -63.188160)
    grafo.agregar(400, "Centro Comercial Chiriguano", -17.790315, -63.205503)
    grafo.agregar(800, "Cine Center", -17.798327, -63.179034)
    grafo.agregar(600, "Las Brisas Centro Comercial", -17.749140, -63.175953)
    grafo.agregar(200, "Centro Comercial Ventura Mall", -17.754422, -63.199559)
    grafo.agregar(500, "Monumento Cristo Redentor", -17.770142, -63.182428)
    grafo.agregar(700, "Catedral Metropolitana Basílica Menor de San Lorenzo", -17.783820, -63.181833)
    return unir(grafo)


def unir(grafo):
    grafo.enlazar(100, 200, peso=11253, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(400, 800, peso=2122, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(700, 800, peso=3158, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(500, 200, peso=12213, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(400, 800, peso=231245, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(600, 700, peso=34583, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(800, 500, peso=1322, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(700, 300, peso=220, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(100, 700, peso=3544, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(500, 600, peso=1856, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(300, 600, peso=243, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(700, 500, peso=3210, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(700, 200, peso=4563, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(200, 800, peso=8632, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(400, 600, peso=853, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(100, 700, peso=85, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(600, 700, peso=941523, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(500, 700, peso=323, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(300, 600, peso=186, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(800, 500, peso=9412, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    grafo.enlazar(200, 100, peso=2342, linea=[[-17.775530, -63.195854], [-17.793336, -63.188160]])
    return grafo


def imprimir(grafo):
    print("Elementos del Grafo\n")
    for elemento in grafo:
        print(elemento)
