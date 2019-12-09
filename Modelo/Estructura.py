class Vertice:

    def __init__(self, clave):
        self.id = clave
        self.conectados = {}

    def getId(self):
        return self.id

    def getConectados(self):
        return self.conectados.keys()

    def getPonderacion(self, vecino):
        return self.conectados[vecino]

    def conectar(self, vecino, ponderacion=0):
        self.conectados[vecino] = ponderacion

    def __str__(self):
        return "ID:" + str(self.id) + \
               " --> Conectados: {" + str([x.id for x in self.conectados]) + "}"


class Grafo:

    def __init__(self):
        self.cantidad = 0
        self.elementos = {}

    def agregar(self, clave):
        self.cantidad = self.cantidad + 1
        vertice = Vertice(clave)
        self.elementos[clave] = vertice
        return vertice

    def obtener(self, index):
        if index in self.elementos:
            return self.elementos[index]
        else:
            return None

    def elementos(self):
        return self.elementos.keys()

    def enlazar(self, elem1, elem2, costo=0):
        if elem1 not in self.elementos:
            nuevo = self.agregar(elem1)
        if elem2 not in self.elementos:
            nuevo = self.agregar(elem2)
        self.elementos[elem1].conectar(self.elementos[elem2], costo)

    def __contains__(self, item):
        return item in self.elementos

    def __iter__(self):
        return iter(self.elementos.values())
