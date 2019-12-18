from Negocio.Organizador import *
from Negocio.Diseñador import *
from Negocio.Graficador import dibujar


def main():
    grafo = construir()
    imprimir(grafo)
    mostrar(grafo)
    # dibujar(grafo)


if __name__ == '__main__':
    main()
