from Negocio.Organizador import *
from Negocio.Graficador import mostrar


def main():
    grafo = construir()
    imprimir(grafo)
    mostrar(grafo)


if __name__ == '__main__':
    main()
